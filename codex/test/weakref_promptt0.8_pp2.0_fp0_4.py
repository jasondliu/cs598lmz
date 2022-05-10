import weakref
# Test weakref.ref() against the most basic class possible

class A(object):

    def __init__(self):
        self.a = 1


class B(object):

    def __init__(self, a):
        self.a = weakref.ref(a)


a = A()
b = B(a)
# 11.3
# Given an array of integers, find the product of its elements.
# Example
# For inputArray = [1, 3, 2, 1, 2], the output should be
# arrayElementsProduct(inputArray) = 12.

def arrayElementsProduct(inputArray):

    product = 1
    for i in inputArray:
        product *= i
    return product

# 11.4
# Find the number of islands.
# An island is a group of adjacent values that are all either
# 1s or 0s. Every cell in the grid can be adjacent to the 4 cells
# that are next to it on the same row or column, as well as the
# 4 cells that are next to it on the diagonals.
# Example
# For

#
