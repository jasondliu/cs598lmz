import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int)

class MyClass(object):
    def __init__(self):
        self.callback = FUNTYPE(self.my_callback)
        self.callback_ptr = ctypes.cast(self.callback,ctypes.c_void_p)
        self.callback_ptr_addr = ctypes.addressof(self.callback_ptr)

    def my_callback(self,x):
        print x
        return x

b = MyClass()
print b.callback_ptr_addr
</code>
The output is:
<code>140733550189648
</code>
Now, when I call <code>callback</code> from <code>MyClass</code> I get the expected output:
<code>b.callback(1)
&gt;&gt;&gt; 1
</code>
However, when I try to call <code>callback</code> from <code>ctypes</code> I get an error:
<code>ctypes.cast(b.callback_ptr_addr,FUNTYPE
