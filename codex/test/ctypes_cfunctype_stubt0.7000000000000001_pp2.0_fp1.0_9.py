import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    if 0:
        return 1
    else:
        return None

def fun2():
    return None

def fun3():
    if 0:
        return 1
    else:
        return

def fun4():
    return

def fun5():
    if 0:
        pass
    else:
        return

def fun6():
    if 0:
        pass
    else:
        return None

def fun7():
    if 0:
        pass
    else:
        return 1

def fun8():
    if 0:
        return
    else:
        return 1

def fun9():
    if 0:
        return 1
    else:
        return 2

def fun10():
    if 0:
        return 1
    else:
        return 1

def fun11():
    if 0:
        return 1
    else:
        return 1
    return 2

def fun12():
    x = 0
    if x:
        return 1
    else:
        return x

