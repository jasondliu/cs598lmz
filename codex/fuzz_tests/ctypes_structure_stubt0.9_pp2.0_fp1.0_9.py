import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p.in_dll(ctypes.cdll.LoadLibrary('libc.so'), "namedValue")
    y = ctypes.c_char_p.in_dll(ctypes.cdll.LoadLibrary('libc.so'), "namedValue")

print(S.x._objects)
print(S.y._objects)
print(S().x)
print(S().y)
print(S.x._objects == S.y._objects)
</code>
What I see is this on my system:
<code>{'libc.so': {'namedValue': 'text'}}
{'libc.so': {'namedValue': 'text'}}
b'text'
b'text'
True
</code>
So they are the same object.

