import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))

def get_callback(func):
    return FUNTYPE(func)


def callback(numbers):
    for i in numbers:
        print(i)
    return 0


if __name__ == '__main__':
    lib = ctypes.cdll.LoadLibrary('./libcallback.so')
    lib.process.argtypes = [FUNTYPE]

    arr = (ctypes.c_int * 3)()
    arr[0] = 0
    arr[1] = 1
    arr[2] = 2

    lib.process(get_callback(callback))

</code>
I want to pass in arr to the callback. I am using C++ as a learning exercise and I choose this topic as it seemed appropriate for learning.


A:

The problem is that you must pass a pointer to the array or use a <code>byref</code> in order to pass the array by reference.
Here is the updated code:
<code>import ctypes
FUNTYPE = ctypes.CF
