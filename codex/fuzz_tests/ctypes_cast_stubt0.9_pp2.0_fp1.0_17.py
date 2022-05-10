import ctypes
ctypes.cast(0, ctypes.py_object)
'''

'''
# List
l = [0]*3
print (l)
'''
'''
t = ((1, 2), (3, 4), (5, 6))

print (t[-1][0])

print ([x ** 2 for x in range(10)])

(a, *b, c) = (0, 1, 2, 3, 4)
print (a, b, c)

(a, b) = (b, a)
print (a, b)

l = [1, (2, 3), (4, (5, 6))]
print ([a for a, *b in l])
print (dict.fromkeys("abc", 1))
'''


'''
l = [1, 2, 3]
print (id(l))

l *= 2

print (l)

print (id(l))
'''
