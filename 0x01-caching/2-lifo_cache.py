#!/usr/bin/env python3
"""
    This class Last-In First-Out
    caching module.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
        LIFOCache that inherits from
        BaseCaching and is a caching system:
    """
    def __init__(self):
        """
            This Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
            Must assign to the dictionary self.cache_data
            the item value for the key key.
            If key or item is None,
            this method should not do anything.
            If the number of items in self.cache_data
            is higher that BaseCaching.MAX_ITEMS:
            you must discard the last item put in
            cache (LIFO algorithm)
            you must print DISCARD: with the key discarded
            and following by a new line
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
            Must return the value in self.cache_data
            linked to key.
            If key is None or if the key doesn’t
            exist in self.cache_data, return None.
        """
        return self.cache_data.get(key, None)
