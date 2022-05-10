import ctypes
ctypes.cast(id(int), ctypes.py_object).value

#7
import collections
a = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
b = collections.Counter('alphabet')

print 'c' in a
print 'c' in b
print a | b

#8
import heapq
a = []
heapq.heappush(a, 5)
heapq.heappush(a, 3)
heapq.heappush(a, 7)
heapq.heappush(a, 4)

print heapq.heappop(a)

heapq.heappushpop(a, 4)
print a
