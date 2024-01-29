#!/usr/bin/env python3
""" Pagination """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ returns tuple of size two containing a start index and an end index """
    end_index = start_index + page_size - 1
    return (start_index, end_index)
