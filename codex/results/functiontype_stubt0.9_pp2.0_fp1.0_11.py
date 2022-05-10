from types import FunctionType
a = (x for x in [1])
b = a.gi_frame
#print(type(b), "gi_frame:", b.f_locals)
print("gi_frame", b.f_locals)
print("gi_running", b.f_lasti)

#print(b.__class__)
#print("dir: ",dir(b.f_locals))
#print("f_locals: ", b.f_locals)
#print("f_lasti :", b.f_lasti)
#print("gc: ",  b.gi_running)
#print("gi_code: ", b.gi_code)
#print("self:", b.gi_yieldfrom) # TypeError: 'generator' object is not callable
#print("frame: ", b.get_frame())
#print("trace: ", b.get_trace())
#print("weakref: ", b.get_weakrefs())
print("hash: ", hash(b))
#print("repr: ", b.repr())
#print("reversed: ", b.reversed())
