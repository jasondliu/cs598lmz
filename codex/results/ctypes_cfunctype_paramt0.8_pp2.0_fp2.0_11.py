import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
def the_callback():
    print('in the_callback()')

reg_type_callback = FUNTYPE(the_callback)
def register(reg_type_callback):
    print('in register()')
    reg_type_callback()
register(reg_type_callback)
</code>
The program runs as:
<code>in register()
in the_callback()
</code>
Now let's comment out the last line, but still pass the callback:
<code>#register(reg_type_callback)
</code>
and we get:
<code>in register()
in the_callback()
</code>
Why doesn't the callback only run when it is registered? (pardon the pun)

