import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
# To get the id of an object, we can use the built-in function id(). The function returns an integer representing the objects identity.
# This identity has to be unique and constant for this object during the lifetime
# The id is assigned to the object when it is created. 
# The is operator compares the identity of two objects; the id is the same when the two objects are the same.
x = (1, 2, 3)
y = (1, 2, 3)
z = x
print(id(x))
print(id(y))
print(id(z))
print(x is y)
print(x is z)

#%%
# If we assign a new value to a variable, the old object will not be affected.
# We can delete the reference to the old object by using the del statement.
# The object then becomes unreachable and will be removed from memory by the garbage collector.
x = (1, 2, 3)
y = (1, 2, 3)
z = x
print(x is y)
print(
