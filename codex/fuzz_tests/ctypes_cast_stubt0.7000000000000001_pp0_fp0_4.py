import ctypes
ctypes.cast(b'a', ctypes.c_char)

# demo_int.py
import ctypes
i = ctypes.c_int(42)
print(i)
print(i.value)
i.value += 1
print(i.value)

# demo_pointer.py
import ctypes
i = ctypes.c_int(42)
p = ctypes.pointer(i)
print(p)
print(p.contents)
p.contents.value += 1
print(p.contents.value)

# demo_array.py
import ctypes
# Create an int array of 3 elements
int_array = ctypes.c_int * 3
i = int_array(1, 2, 3)
print(i[0], i[1], i[2])

# demo_cast.py
import ctypes
# Create a pointer to an integer
i = ctypes.c_int(42)
p = ctypes.pointer(i)
print(p)
print(p.contents)
p.contents.value += 1
print(
