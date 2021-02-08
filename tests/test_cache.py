import phicache
import pytest


DATA1 = {'id': 1, 'name': 'name1'}
DATA1_2 = {'id': 1, 'name':'name1_2'}
DATA2 = {'id': 2, 'name': 'name2'}
DATA2_2 = {'id': 2, 'name': 'name2_3'}


assert type(DATA1) is type(DATA1_2) is type(DATA2) is type(DATA2_2)


@pytest.fixture
def cache():
    return phicache.Cache(type(DATA1))


def test_cache_init(cache: phicache.Cache):
    assert cache.data_type is type(DATA1)
    assert type(cache.cache) is dict


def test_cache_len(cache: phicache.Cache):
    assert len(cache) == len(cache.cache)


def test_cache_setitem(cache: phicache.Cache):
    with pytest.raises(ValueError):
        cache[DATA1['id']] = 1
    cache[DATA1['id']] = DATA1
    cache[DATA1['id']] = DATA1_2

    assert len(cache.cache[DATA1['id']]) == 2


def test_cache_getitem(cache: phicache.Cache):
    cache[DATA1['id']] = DATA1
    cache[DATA1['id']] = DATA1_2

    cache[DATA2['id']] = DATA2
    cache[DATA2['id']] = DATA2_2

    assert cache[DATA1['id'], phicache.Strategy.LATEST] == DATA1_2
    assert cache[DATA1['id'], phicache.Strategy.OLDEST] == DATA1
    assert cache[DATA1['id'], phicache.Strategy.MOST_RECENT_ACCESS] == DATA1
    assert cache[DATA1['id'], phicache.Strategy.OLDEST_ACCESS] == DATA1_2

    assert cache[DATA2['id'], phicache.Strategy.OLDEST] == DATA2
    cache[DATA2['id'], phicache.Strategy.OLDEST]
    cache[DATA2['id'], phicache.Strategy.OLDEST]
    cache[DATA2['id'], phicache.Strategy.OLDEST]
    assert cache[DATA2['id'], phicache.Strategy.MOST_ACCESSED] == DATA2
    assert cache[DATA2['id'], phicache.Strategy.LEAST_ACCESSED] == DATA2_2


def test_cache_contains():
    cache = phicache.Cache(int)
    cache[1] = 2
    assert 1 in cache
    assert 2 not in cache


def test_cache_non_type_enforcing():
    cache = phicache.Cache()
    cache[1] = 1
    cache['lorem'] = 'ipsum'
    cache['lorem'] = 'dolor'

    assert cache['lorem', phicache.Strategy.OLDEST] == 'ipsum'
    assert cache['lorem', phicache.Strategy.LEAST_ACCESSED] == 'dolor'
    assert cache[1] == 1
