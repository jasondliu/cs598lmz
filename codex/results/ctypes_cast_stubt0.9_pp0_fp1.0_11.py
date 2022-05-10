import ctypes
ctypes.cast(pointer, ctypes.POINTER(type))
</code>
You can even write a function that casts the array for you:
<code>def cast_to(arr, ctype):
    return (ctype * len(arr)).from_address(arr.__array_interface__['data'][0])
</code>

