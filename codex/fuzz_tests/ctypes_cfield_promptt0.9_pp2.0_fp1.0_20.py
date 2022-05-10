import ctypes
# Test ctypes.CField
assert(ctypes.CField == ctypes.Structure)
# Test fields (in objc)
assert(cobj.fields == ('a', 'b'))
assert(ctype(pobj.a))
assert(ctype(pobj.b))
# Test 'struct' keyword
s = ctypes.create_string_buffer('abc')
# Test sizeof
for ob in [ctypes.CField, cob, pobj]:
    assert(ctypes.sizeof(ob) == s.value)

# Test objc_msgSend (__typestr__)
def_send = ctypes.objc_msgSend
assert(def_send(def_send, def_send, def_send, def_send) == def_send)
oc_obj = msg_send.callable(id, 'alloc')
assert(msg_send(oc_obj, 'init'))
assert(def_send(oc_obj, def_send, def_send, def_send) == def_send)
# Clean up
del def_send, oc_obj

# Test 'NS
