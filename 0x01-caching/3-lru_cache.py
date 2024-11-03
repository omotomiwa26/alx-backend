#!/usr/bin/env python3
"""
    This class Least Recently Used caching module.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
        LRUCache that inherits from BaseCaching and
        is a caching system:
    """
    def __init__(self):
        """
            This  Initializes the cache.
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
            you must discard the least recently used item (LRU algorithm)
            you must print DISCARD: with the key discarded
            and following by a new line
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
            Must return the value in self.cache_data
            linked to key.
            If key is None or if the key doesn’t
            exist in self.cache_data, return None.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
