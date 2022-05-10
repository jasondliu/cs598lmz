import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_int)


def foo(x):
    return x + 1


raw_func = FUNTYPE(foo)
print(raw_func('hello', 123))
</code>
This works fine. However, when I change the return type of <code>foo</code> to <code>str</code> (or any other Python type) I get a <code>TypeError: Don't know how to convert function return value to a C return type.</code> error.
Why does it work for <code>int</code> but not for other types?

