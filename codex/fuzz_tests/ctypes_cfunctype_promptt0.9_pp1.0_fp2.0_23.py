import ctypes
# Test ctypes.CFUNCTYPE

# Creates the required argtypes and restype for each function.
for type in ['id', 'Class', 'SEL', 'BOOL', 'void']:
    locals()['A_%s' % type] = ctypes.CFUNCTYPE(locals()[type])
    locals()['B_%s' % type] = ctypes.CFUNCTYPE(locals()[type], 
                                                                ctypes.c_int)
    locals()['C_%s' % type] = ctypes.CFUNCTYPE(locals()[type], 
                                                                ctypes.c_int, 
                                                                ctypes.c_int)

# Tests the created argtypes and restype.
def test_A():
    for type in ['id', 'Class', 'SEL', 'BOOL', 'void']:
        temp = locals()['A_%s' % type](temp)
    
def test_B():
    for type in ['id', 'Class', 'SEL', 'BOOL', 'void']:
       
