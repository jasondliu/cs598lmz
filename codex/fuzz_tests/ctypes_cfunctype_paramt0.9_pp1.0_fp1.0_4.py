import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

doubleIt = FUNTYPE(lib.DoubleIt)

def test_BLA():
    assert doubleIt(0) == 0
    assert doubleIt(2.0) == 4.0
    assert doubleIt(2.0) == 4.0


def test_compare_pythran_and_c(compare_c_functions):
    DUMMY_INTEGER = 1
    DUMMY_FLOAT = 1.0
    DUMMY_STRING = "string"

    def pythran_function(*args):
        return args
    pythran_function = pythran_function.pythran()

    @compare_c_functions(pythran_function)
    def c_function(*args):
        lib.pythran_print_int(DUMMY_INTEGER)
        lib.pythran_print_float(DUMMY_FLOAT)
        lib.pythran_print_string(DUMMY_STRING)
        return args
