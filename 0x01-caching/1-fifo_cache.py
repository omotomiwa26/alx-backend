#!/usr/bin/env python3
"""
    This class FIFO caching inherits
    from BaseCaching
"""


from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
        FIFO Cache that inherits from BaseCaching
        and is a caching system
    """
    def __init__(self):
        """
            This initializies the cache
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
            you must discard the first item put in cache (FIFO algorithm)
            you must print DISCARD: with the key discarded
            and following by a new line
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """
            Must return the value in self.cache_data linked to key.
            If key is None or if the key
            doesn’t exist in self.cache_data, return None.
        """
        return self.cache_data.get(key, None)
