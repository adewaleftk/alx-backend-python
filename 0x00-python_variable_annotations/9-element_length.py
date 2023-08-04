#!/usr/bin/env python3
'''Task 9'''
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    '''List of string returns a List of Tuple'''
    return [(i, len(i)) for i in lst]
