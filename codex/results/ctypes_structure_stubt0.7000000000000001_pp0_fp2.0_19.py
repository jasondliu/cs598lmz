import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(0)
    y = ctypes.c_int(0)

# create a S object
S_obj = S()
S_obj.x = 1
S_obj.y = 2

# get the address of the object
address = ctypes.addressof(S_obj)

# cast the address as a POINTER(S) and dereference it
S_ptr = ctypes.POINTER(S).from_address(address)
print(S_ptr.contents.x, S_ptr.contents.y)

# change the values
S_ptr.contents.x = 3
S_ptr.contents.y = 4
print(S_ptr.contents.x, S_ptr.contents.y)

# check the values of the original object
print(S_obj.x, S_obj.y)
```

Produces the output:
```
1 2
3 4
3 4
```

### Using the from_buffer method

The from_buffer method is used in the following manner:

