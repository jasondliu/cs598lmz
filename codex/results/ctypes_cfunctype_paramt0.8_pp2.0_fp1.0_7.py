import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_int)

def cb_func(b,c):
    print("In python callback func:\n")
    print("b:",b," c:",c)
    #return b+c
    pass

cb_func_ptr = FUNTYPE(cb_func)
dllobj = ctypes.CDLL('libc_module.so')
dllobj.run_callback(cb_func_ptr)
</code>
libc_module.c
<code>#include &lt;stdio.h&gt;

typedef int (*callback_t)(int,int);

int run_callback(callback_t func){
    int d;
    //d = func(1,2);
    printf("In C callback func\n");
    return 0;
}
</code>
output:
<code>$ python3 main.py 
In C callback func
</code>
You can't just do <code>func(1,2)</code> in C to call the callback because it's
