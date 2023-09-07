"""
Name: binarysearch
Author: Michael Barthauer
Date: 9/6/2023
Description: Locates a given value in a sorted list using binary search.
"""


def binarysearch(arr, n, k):
    # check that k actually has a chance of being in the list
    if (k < arr[0]) or (k > arr[-1]):
        return -1
    i = n // 2  # index of current element
    start = 0  # beginning of current list segment
    end = n  # length of current list segment
    # begin binary search
    while True:
        if k == arr[i]:
            return i  # found it!
        if (end - start) == 1:
            return -1  # out of options
        if k < arr[i]:
            # not present in right half of current segment
            end = i
            # subdivide further
            i = start + ((end - start) // 2)
        elif k > arr[i]:
            # not present in left half of current segment
            start = i
            # subdivide further
            i = start + ((end - start) // 2)
