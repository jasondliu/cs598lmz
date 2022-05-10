import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char()

a = S()
a.x = b'a'
print(a.x)
#=&gt; b'a'

a.x = 'a'
print(a.x)
#=&gt; b'a'

a.x = 'a'.encode()
print(a.x)
#=&gt; b'a'

a.x = 'a'.encode().decode()
print(a.x)
#=&gt; b'a'
</code>

