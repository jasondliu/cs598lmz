import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 5
type(fun)

# ctypes acts as a very thin layer around ffi. No need to learn anything more than in the cookbook

# https://langui.sh/2009/03/13/ctypes-tutorial-part-1/ also has a tutorial but it probably won't help

# TODO: TUTORIAL HERE FOR SOME REASON


def callback(name):
    print(name)
    return name

lib.CallMeBack(callback)

# TODO: TUTORIAL for C

# and now for the second part
# https://www.toptal.com/python/managing-python-memory-with-ctypes

import numpy as np

matrix = np.random.rand(6, 250, 250).astype(np.float32)

print(matrix)

ptr = lib.AllocateMatrix(matrix)
new_matrix = lib.GetMatrix(ptr)

print(new_matrix)
