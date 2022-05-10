import ctypes
ctypes.cast(1, ctypes.py_object)

#3.5.2
import sys
sys.getrefcount(1)

#3.5.3
a = [1, 2, 3]
b = a
a.append(4)
b

#3.5.4
a = None

#3.5.5
import ctypes
def ref_count(address):
    return ctypes.c_long.from_address(address).value

ref_count(id(a))

#3.5.6
b = [1, 2, 3]
ref_count(id(b))

#3.5.7
import sys
sys.getrefcount(1)

#3.6.1
class BinaryNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#3.6.2
node = BinaryNode(10)

#3.6.3
