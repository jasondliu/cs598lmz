import ctypes
ctypes.cast(pointer, ctypes.pointer(buffer))
</code>
However, buffer looks the same as it did before. Nothing has been copied into it. 
I've read that I need to set the buffer to read the whole structure, and then I should be able to cast the pointer to it, but I haven't been able to find a way to do that.
Is there a way to set buffer so it can store the entire structure?


A:

You're right that you need to ensure that the buffer is large enough. You can use the <code>sizeof</code> helper function for that:
<code>import ctypes

class Demo(ctypes.Structure):
    _fields_ = [
        ('field_one', ctypes.c_int),
        ('field_two', ctypes.c_double)
    ]


buffer = ctypes.create_string_buffer(ctypes.sizeof(Demo))
pointer = lib.do_something()

# we can't use pointer/Demo directly, as it's a void pointer.
# instead, copy its value into a ctypes.c_void_p
