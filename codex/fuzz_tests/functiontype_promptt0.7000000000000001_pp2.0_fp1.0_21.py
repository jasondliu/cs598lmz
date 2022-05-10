import types
# Test types.FunctionType
import types
def f(): pass
def g1(): f()
def g2(): f
def g3(): pass # test unreachable code
print isinstance(f, types.FunctionType)
print isinstance(g1, types.FunctionType)
print isinstance(g2, types.FunctionType)
print isinstance(g3, types.FunctionType)

print isinstance(f(), types.FunctionType)
print isinstance(g1(), types.FunctionType)
print isinstance(g2(), types.FunctionType)
print isinstance(g3(), types.FunctionType)

print types.FunctionType
print types.FunctionType
print types.FunctionType
print types.FunctionType

# Test types.GeneratorType
import types
def gen():
    i = 0
    while 1:
        yield i
        i+=1

g = gen()
g.next()
g.next()

print isinstance(gen, types.GeneratorType)
print isinstance(g, types.GeneratorType)
print isinstance(gen(), types.GeneratorType)
print isinstance
