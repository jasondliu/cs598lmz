import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_crash():
    # ctypes calls the function with a borrowed reference to the result,
    # and the result is a borrowed reference to None.  So the following
    # call should crash.
    fun()

def main():
    test_crash()

main()
