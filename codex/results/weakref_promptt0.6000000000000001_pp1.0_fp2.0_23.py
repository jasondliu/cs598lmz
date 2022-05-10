import weakref
# Test weakref.ref(dict)

class Dict(dict):
    pass

class Weak(object):
    pass

d = Dict()
w = Weak()

d['dict'] = d
d['weak'] = w
w.d = d

rd = weakref.ref(d)
rw = weakref.ref(w)

print rd(), rw()

del d
del w

print rd(), rw()

del rd
del rw

print Dict.__module__
