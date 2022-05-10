import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def myfunc(a, b):
    print("Hello from Python!")
    return a + b

myfunc_c = FUNTYPE(myfunc)
</code>
Now, I can pass this function to C code and call it:
<code>#include &lt;stdio.h&gt;

int call_func(int (*f)(int, int)) {
    return f(1, 2);
}

int main(int argc, char *argv[]) {
    printf("%d\n", call_func(myfunc_c));
    return 0;
}
</code>
This works fine, but I'd like to be able to pass a function with a different signature. I've tried to use <code>ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)</code> but I get the following error:
<code>TypeError: &lt;built-in function CFUNCTYPE&gt;: don't know
