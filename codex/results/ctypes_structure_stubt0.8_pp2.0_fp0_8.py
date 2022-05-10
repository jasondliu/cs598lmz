import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    _fields_ = [('x', ctypes.c_int)]

if __name__ == "__main__":
    # This works when we initialize a new variable
    a = S()
    a.x = 1
    print a.x

    # But in this case, we have an old variable, without its fields initialized
    b = S.from_buffer(ctypes.c_buffer(4))
    try:
        print b.x
    except ValueError:
        print "excepted error"
