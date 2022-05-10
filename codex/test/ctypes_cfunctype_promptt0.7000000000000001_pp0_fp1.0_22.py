import ctypes
# Test ctypes.CFUNCTYPE
# The function should return a string.
def test_CFUNCTYPE():
    # This is the function that will be called.
    def func(n):
        return "hello " + str(n)
    # This is the type of the function argument.
    # The ctypes module defines c_int, c_char_p, and more.
    T_ARG = ctypes.c_int
    # This is the type of the function's return value.
    T_RESULT = ctypes.c_char_p
    # Create the function type, and create the callback function.
    # The first argument is the function type, and the second is the function.
    # The result is the callback function.
    cbfunc = ctypes.CFUNCTYPE(T_RESULT, T_ARG)(func)
    # Call the callback function.
    result = cbfunc(42)
    # Check the result.
    assert result == "hello 42"
