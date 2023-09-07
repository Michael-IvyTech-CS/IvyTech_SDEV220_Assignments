"""
Name: sort012
Author: Michael Barthauer
Date: 9/6/2023
Description: Sorts a given array of length N containing 0s, 1s, and 2s in ascending order.

Assumptions: Not allowed to use built in sort() function.
"""


def sort012(arr, n):  # implements a fairly trivial sorting algorithm
    zeros = 0
    ones = 0
    twos = 0
    # count the number of zeros, ones, and twos present
    for i in arr:
        if i == 0:
            zeros += 1
        elif i == 1:
            ones += 1
        elif i == 2:
            twos += 1
    arr.clear()  # clear out unsorted contents
    arr.extend([0] * zeros)  # append all the zeros
    arr.extend([1] * ones)  # append all the ones
    arr.extend([2] * twos)  # append all the twos
