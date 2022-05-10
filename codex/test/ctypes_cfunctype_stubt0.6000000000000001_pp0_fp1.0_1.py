import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

def example_c():
    return ctypes.pythonapi.PyRun_SimpleString(ctypes.c_char_p(b"print('Hello')"))

def example_py():
    return exec("print('Hello')")

if __name__ == "__main__":
    print(fun())
    print(example_c())
    print(example_py())
