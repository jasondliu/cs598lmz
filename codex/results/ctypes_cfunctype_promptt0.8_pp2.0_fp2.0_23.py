import ctypes
# Test ctypes.CFUNCTYPE(), and make sure ctypes.cast() can be applied to functions.

from ctypes import *

int_array10 = c_int * 10

class TestFuncPtr(unittest.TestCase):
    def test_cfunctype(self):
        # define a function type, a function of 2 int returning an int
        CMPFUNC = CFUNCTYPE(c_int, c_int, c_int)

        # initialize a ctypes array of 3 ints
        array3 = int_array10()
        for i in range(len(array3)):
            array3[i] = i * i
        # print the array
        for i in array3:
            print(i)

        # sort the array with qsort, with function compare taking 2 ints
        # returning int, and taking an extra data argument of type void *
        qsort = CDLL(ctypes.util.find_msvcrt()).qsort
        qsort.argtypes = c_void_p, c_size_t, c_size_t, CMPFUNC

