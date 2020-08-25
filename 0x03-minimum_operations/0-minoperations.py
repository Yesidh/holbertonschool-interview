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

    if not isinstance(n, int) or n <= 1:
        return 0

    copy_paste = 0
    prime_factors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                     53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 113]
    i = 0

    while n > 1 and i <= 25:
        if n % prime_factors[i] == 0:
            copy_paste += prime_factors[i]
            n /= prime_factors[i]
        else:
            i += 1

    if n == 1:
        return int(copy_paste)
    else:
        return int(copy_paste + n)