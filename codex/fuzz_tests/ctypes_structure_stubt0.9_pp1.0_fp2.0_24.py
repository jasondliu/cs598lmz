import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    i = ctypes.c_int()
    f1 = ctypes.c_float()
    f2 = ctypes.c_float()

#s = S(i=3) # TypeError: Type S takes no arguments
s = S()
s.i = 3
print s.i # 3
print s.x # 0
#s.f1 = 3 # AttributeError: f1
print s.f2 # 0.0
</code>
I'd expect the last line to give me a TypeError as well, since I never set <code>s.f1</code> and it's not a valid attribute (it doesn't exist yet)


A:

There's nothing special happening here.  Ctypes is just treating instances of the <code>S</code> structure as instances of <code>Structure</code>, which provides a default <code>__getattr__</code> implementation.  See this answer I wrote a while back:
https://stackoverflow.com/a/2181605/2988730

