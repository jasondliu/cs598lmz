import ctypes
ctypes.cast(ctypes.pointer(a), ctypes.POINTER(ctypes.c_double)).contents = 3.14
assert a.value == 3.14

c = [1, 2, 3]
a = np.arange(5)
a.__array_interface__['data'][0] = c
assert a.tolist() == [1, 2, 3, 3, 4]

n = np.arange(15)
class T(object): pass
t = T()
t.array = n.reshape(3,5)
assert t.array.shape == (3, 5)
n.shape = 5, 3
assert t.array.shape == (5, 3)
assert t.array[4, 2] == 14

n = np.arange(15)
assert n.item(4, 2) == 12
n.itemset((4, 2), 999)
assert n[4, 2] == 999

# From: https://www.python.org/download/releases/2.3/mro/
class A(object):
    def __
