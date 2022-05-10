import ctypes
# Test ctypes.CFUNCTYPE type

import ctypes as C

# Simple callback
CB_FUNC = C.CFUNCTYPE(C.c_int, C.POINTER(C.c_int))

def print_address(n):
    print '%d: 0x%x' % (n, C.addressof(n))
    return 0

print_address_cb = CB_FUNC(print_address)

# Call the callback
print_address_cb(C.pointer(C.c_int(42)))

# Check that the callback is still alive
print_address_cb(C.pointer(C.c_int(42)))

# Yes, we're cheating here...
print "function-object(print_address_cb):",
print print_address_cb
print "function-object(print_address):",
print print_address_cb.__closure__[0].cell_contents

# Make sure we can store the callback in a dict...
d = {'callback': print_address_cb, 'data': 12345}
print d['callback']
print d
