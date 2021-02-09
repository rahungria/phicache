from .cache_item import CacheItem
from .strategy import Strategy


__all__ = 'Cache',


class Cache:
    def __init__(self, data_type: type=None, default_strategy=Strategy.MOST_RECENT_ACCESS):
        # TODO allow forward declaring type to lazily enforce type
        self.data_type = data_type
        self.default_strategy = default_strategy
        self.cache = dict()

    def __len__(self):
        return len(self.cache)
    
    def __getitem__(self, key):
        '''
        to get a cached item
        '''
        if type(key) is tuple:
            k, strategy = key
        else:
            k = key
            strategy = self.default_strategy

        cache_items: list[CacheItem] = self.cache[k]

        if not cache_items:
            raise KeyError(f"Cache Empty at '{key}'")

        # Cache Access Strategy switch case
        if strategy == Strategy.MOST_RECENT_ACCESS:
            most_recent_access = cache_items[0]
            for item in cache_items:
                if item.last_access > most_recent_access.last_access:
                    most_recent_access = item
            return most_recent_access.access()
        elif strategy == Strategy.OLDEST_ACCESS:
            oldest_access = cache_items[0]
            for item in cache_items:
                if item.last_access < oldest_access.last_access:
                    oldest_access = item
            return oldest_access.access()
        elif strategy == Strategy.LATEST:
            latest = cache_items[0]
            for item in cache_items:
                if item.created > latest.created:
                    latest = item
            return latest.access()
        elif strategy == Strategy.OLDEST:
            oldest = cache_items[0]
            for item in cache_items:
                if item.created < oldest.created:
                    oldest = item
            return oldest.access()
        elif strategy == Strategy.MOST_ACCESSED:
            most_accessed = cache_items[0]
            for item in cache_items:
                if item.accesses > most_accessed.accesses:
                    most_accessed = item
            return most_accessed.access()
        elif strategy == Strategy.LEAST_ACCESSED:
            least_accessed = cache_items[0]
            for item in cache_items:
                if item.accesses < least_accessed.accesses:
                    least_accessed = item
            return least_accessed.access()
        else:
            raise KeyError(
                'Passed Invalid Argument for Cache Strategy in '
                'Cache.__getitem__(key, strategy)... '
                'Use Strategy Enum.'
            )

    def __setitem__(self, key, value):
        if self.data_type:
            if not issubclass(type(value), self.data_type):
                raise ValueError(
                    f'cache type must match declared data_type: {self.data_type}'
                )
        if key not in self.cache:
            # TODO maybe replace list for priority queue for each strategy:
            # reduce access time from O(n) to O(1) (but space complexity
            # from O(1) to O(n), with n being the ammount of strategies)
            self.cache[key] = []
        self.cache[key].append(CacheItem(value))

    def __repr__(self):
        return repr(self.cache)

    def __str__(self):
        rtrn = {}
        for key in self.cache:
            rtrn[key] = []
            for item in self.cache[key]:
                rtrn[key].append(str(item))
        return str(rtrn)

    def __iter__(self):
        return self.cache.__iter__()

    def __reversed__(self):
        return self.cache.__reversed__()

    def __contains__(self, item):
        return item in self.cache
