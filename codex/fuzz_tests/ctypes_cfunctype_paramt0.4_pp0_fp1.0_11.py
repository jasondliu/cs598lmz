import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(i):
    print "callback", i
    return i

CALLBACK = FUNTYPE(callback)

# lib = ctypes.CDLL("./libtest.so")
lib = ctypes.CDLL("/home/jason/workspace/c/test/libtest.so")
lib.test(CALLBACK)
</code>
The error message is:
<code>Traceback (most recent call last):
  File "./test.py", line 14, in &lt;module&gt;
    lib.test(CALLBACK)
ctypes.ArgumentError: argument 1: &lt;type 'exceptions.TypeError'&gt;: Don't know how to convert parameter 1
</code>


A:

You need to declare the function prototype in C.
<code>typedef int (*callback_t)(int);

void test(callback_t callback) {
    callback(42);
}
</code>
Then in Python, you can use <code>CALL
