import types
# Test types.FunctionType
# Found by Greg Ewing <greg.ewing@canterbury.ac.nz>

def f(): pass
g = f.func_code

def g(): pass
f = g.func_code

del g
del f
