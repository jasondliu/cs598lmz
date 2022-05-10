import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int32,ctypes.c_int32,ctypes.c_int32)

def set_callback():
    callback = FUNTYPE(callback_c)
    lib.set_callback(callback)

if __name__ == '__main__':
    set_callback()
    lib.call_callback(1, 2)
</code>
test.c:
<code>#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;

void set_callback(int (*callback)(int, int));
void call_callback(int a, int b);

int callback_c(int a, int b){
    printf("callback_c(%d, %d)\n", a, b);
    return a*b;
}

void set_callback(int (*callback)(int, int)){
    printf("set_callback(%p)\n", (void *)callback);
    callback(6, 7);
}

void call_callback(int a, int b){
    printf("call_callback(%
