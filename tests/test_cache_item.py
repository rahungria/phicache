import phicache
import pytest
import datetime


@pytest.fixture
def item():
    data = {'id': 1, 'name': 'name'}
    return phicache.CacheItem(data)


def test_cache_item_init(item: phicache.CacheItem):
    assert item.accesses == 0
    assert type(item.data) is dict
    assert item.data == {'id': 1, 'name': 'name'}
    assert type(item.last_access) is datetime.datetime
    assert type(item.created) is datetime.datetime
    assert item.last_access == item.created


def test_cache_item_repr(item: phicache.CacheItem):
    _repr = eval(repr(item))
    assert 'data' in _repr
    assert 'accesses' in _repr
    assert 'created' in _repr
    assert 'last_access' in _repr

    assert _repr['data'] == item.data
    assert _repr['accesses'] == item.accesses
    assert _repr['created'] == item.created
    assert _repr['last_access'] == item.last_access


def test_cache_item_str(item: phicache.CacheItem):
    _str = str(item)
    assert "'data':" in _str
    assert str(item.data) in _str
    assert "'accesses':" in _str
    assert str(item.accesses) in _str
    assert "'created':" in _str
    assert str(item.created) in _str
    assert "'last_access':" in _str
    assert str(item.last_access) in _str


def test_cache_item_access(item: phicache.CacheItem):
    _created = item.created
    _last_access = item.last_access
    _accesses = item.accesses
    assert item.data == item.access()
    assert _created == item.created
    assert _last_access != item.last_access
    assert item.accesses == _accesses+1
