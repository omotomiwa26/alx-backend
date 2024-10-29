#!/usr/bin/env python3
"""
    This function Simple pagination Copy index_range
    from task 0-simple_helper_function.py
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Page numbers are 1-indexed,
        the first page is page 1.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """
        Server class to paginate a database of
        popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
            Initializes a new Server instance.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
            Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            This method Implement a method named get_page
            that takes two integer arguments page with default value
            1 and page_size with default value 10..
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]
