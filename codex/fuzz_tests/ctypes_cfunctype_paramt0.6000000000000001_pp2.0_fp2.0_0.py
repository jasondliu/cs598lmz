import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def MyFunc(x):
    print("MyFunc called with:", x)
    return 42

a = FUNTYPE(MyFunc)
print("Calling a...")
print("    a(1) =", a(1))
print("Calling a again...")
print("    a(2) =", a(2))

print("Setting a to None")
a = None
print("Calling a...")
print("    a(1) =", a(1))
</code>
Output:
<code>Calling a...
MyFunc called with: 1
    a(1) = 42
Calling a again...
MyFunc called with: 2
    a(2) = 42
Setting a to None
MyFunc called with: 1
    a(1) = 42
</code>

