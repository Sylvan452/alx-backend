#!/usr/bin/python3

''' 1-fifo_cache.py script'''

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    ''' FIFO Cache '''

    def __init__(self):
        ''' self initialization Method '''
        super().__init__()
        self.keys = []

    def put(self, key, item):
        ''' Add k-v pair to cache '''
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        ''' Return value from cache '''
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
