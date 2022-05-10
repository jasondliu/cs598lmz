import ctypes
ctypes.cast(0, ctypes.py_object).value

#%%
from ctypes import py_object
t = py_object(3)
t.value

#%%
t = [1,2,3]
ctypes.cast(id(t), ctypes.py_object).value

#%%
def test():
    return 7

test()

#%%
def test():
    return 7
    return 8

test()

#%%
def test():
    try:
        return 7
    finally:
        return 8
    
test()

#%%
def test():
    try:
        return 7
    except:
        return 8
    finally:
        return 9
    
test()

#%%
def test():
    try:
        return 7
    except:
        return 8
    return 9
    
test()

#%%
def test():
    try:
        return 7
    except:
        return 8
    return 9
    raise TypeError
    
test()

#%%
def test():
    return 7
    raise
