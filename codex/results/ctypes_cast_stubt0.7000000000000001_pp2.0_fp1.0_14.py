import ctypes
ctypes.cast(rv, ctypes.py_object).value

# The last step is to manipulate the result using Python's standard string operations, indicated by the trailing s; this expression turns the bytes data into a string:
s = rv.tobytes()
print(s)

# The previous example is a bit low-level. In practice, we can get the same result more easily by using the built-in bytes type and specifying an encoding:
t = bytes('Hello, World', encoding='utf-8')
print(t)

# If we require a true mutable byte array, then we need to use bytearray instead:
b = bytearray(b'Hello, World')
print(b)

# The bytearray type, like bytes, is immutable. So, the following code produces an error:
b[0] = ord('J')
print(b)

# To append to a byte array, we need to use the append method:
b.append(ord('!'))
b

# To modify an existing byte array, we need to use the extend method.
b.extend(b'
