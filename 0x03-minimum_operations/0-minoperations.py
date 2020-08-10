#!/usr/bin/python3
"""
==================================
only minOperations function inside
==================================
"""


def minOperations(n):
    """
    return an integer with fewest number of operations
    needed to result in exactly n H characters
    """

    if not isinstance(n, int) or n <= 0 or n == 1:
        return 0
    else:
        if (n % 5) == 0:
            if n == 5:
                return 5
            else:
                return int((n / 5) - 1) + 6
        elif (n % 3) == 0:
            if n == 3:
                return 3
            else:
                return int((n / 3) - 1) + 4
        elif (n % 2) == 0:
            if n == 2:
                return 2
            else:
                return int((n / 2) - 1) + 3
        else:
            return 0
