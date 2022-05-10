import ctypes
ctypes.cast(0, ctypes.c_int).value

# from struct import *
# pack('hhl', 1, 2, 3)
# unpack('hhl', '\x00\x01\x00\x02\x00\x00\x00\x03')


# from array import array
# a = array('i', [1, 2, 3])
# a[2]
# a.append(4)
# print a

# from bisect import *
# a = [1, 2, 2, 2, 3, 4, 7]
# print bisect_left(a, 2)
# print bisect_right(a, 2)
# insort(a, 5)
# print a

# from heapq import *
# heap = []
# data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# for item in data:
#     heappush(heap, item)
# heappop(heap)
# heapreplace(heap, 0.5)
# print heap

# from collections
