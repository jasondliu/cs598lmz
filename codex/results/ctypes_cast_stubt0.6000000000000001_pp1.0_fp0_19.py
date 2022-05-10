import ctypes
ctypes.cast(id(x), ctypes.py_object).value

np.shares_memory(x, x_np)
 
# We can see that they share the same memory space!

# NOTE: If we change the np.ndarray into a Python list, they will NOT share the same memory space!

# We can also use the built-in Python function id() to get memory locations

print('id(x) =', id(x))
print('id(x_np) =', id(x_np))
 
x[0] = 100

x_np
 
# We see that if we change the value of x[0], the corresponding value in x_np also changes!
 
# Similarly, we can create a numpy ndarray from a Python list

y = np.array([1,2,3,4,5])
y
 
# And we can again check if they share the same memory space

np.shares_memory(y, [1,2,3,4,5])
 
# We see that they do not share the same memory space!
 
