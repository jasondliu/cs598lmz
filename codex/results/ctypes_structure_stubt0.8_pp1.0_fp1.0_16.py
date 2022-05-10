import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int


if __name__ == "__main__":
    import sys
    import support
    support.set_platform_path()
    a = S()
    error = 0
    try:
        exec("a.x = ''")
    except TypeError:
        error = 1
    else:
        error = 0
    if error == 0:
        raise support.TestError("Field assignment with non-matching type should fail")

    a = S()
    error = 0
    try:
        exec("a.x = 10")
    except ValueError:
        error = 1
    else:
        error = 0
    if error == 0:
        raise support.TestError("Field assignment with out-of-range integer value should fail")
