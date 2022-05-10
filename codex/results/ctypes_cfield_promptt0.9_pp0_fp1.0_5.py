import ctypes
# Test ctypes.CField variable
g_cfi = ctypes.CField()
print type(g_cfi)

# Test function variable
g_fn = ctypes.function()
print type(g_fn)

# XXX: ctypes.variable() isn't used anywhere in the code, check if needed elsewhere. 
# Test variable variable
g_var = ctypes.variable()
print type(g_var)

# Test CStruct variable
g_cst = ctypes.type()
g_cst.type_name = 'abc'
g_cst.type_stream = ''
g_cst.type_hash = ""
g_cst.fields = {}
g_cst.field_order = []
print type(g_cst)

# Test Primitive type variable
g_ptt = ctypes.primitive()
print type(g_ptt)

# Test Container type variable
g_ctt = ctypes.container()
print type(g_ctt)

# Test Union type variable
g_utt = ctypes.un_type()
print type(g_
