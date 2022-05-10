import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.py_object)


def main():
    # The function signature for the callback function
    cbfun = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.py_object)

    # A callable built from cbfun
    # which has to be registered with the C library
    @cbfun
    def foo(arg):
        print('1', arg)
        return 42

    @cbfun
    def bar(arg):
        print('2', arg)
        return 100

    # Register the function
    register_fun(foo)

    # Register a different function (unregisters foo)
    register_fun(bar)

    # Register the first function again
    register_fun(foo)

    # Call the function
    result = myfun(42)
    print('result', result)


if __name__ == '__main__':
    main()
</code>

