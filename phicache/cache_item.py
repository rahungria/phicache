from datetime import datetime


__all__ = 'CacheItem',


class CacheItem:
    def __init__(self, data):
        self.data = data
        self.accesses = 0
        now = datetime.now()
        self.created = now
        self.last_access = now

    def access(self):
        self.accesses += 1
        self.last_access = datetime.now()
        return self.data

    def __repr__(self):
        return repr({
            'data': self.data,
            'accesses': self.accesses,
            'created': self.created,
            'last_access': self.last_access,
        })

    def __str__(self):
        return str({
            'data': str(self.data),
            'accesses': self.accesses,
            'created': str(self.created),
            'last_access': str(self.last_access),
        })
