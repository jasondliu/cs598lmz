import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x**2

# Create a C double array of the right size
c_data = (ctypes.c_double * len(data))()

# Fill it with the data
for i in range(len(data)):
    c_data[i] = data[i]

# Create a function pointer
f = FUNTYPE(func)

# Call the C function
c_func(f, c_data, len(data))

# Convert the C array back to a Python list
print [c_data[i] for i in range(len(data))]
</code>

