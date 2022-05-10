gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & 0x20)
print(gi.gi_code.co_flags)

print(gi.gi_code.co_varnames)

#generator-iterator
print("#generator-iterator")
def g():
    yield 1
print(type(g()))
print(type(iter(g())))

#generator-iterable
print("#generator-iterable")
def g():
    yield 1
print(isinstance(g(), collections.abc.Iterable))
print(isinstance(g(), collections.abc.Iterator))

#generator-expressions
print("#generator-expressions")

def _some_gen():
    yield 1
    return

print(isinstance(_some_gen, collections.abc.Generator))
print(isinstance((i for i in ()), collections.abc.Generator))

#generator-expressions-iterable
print("#generator-expressions-iterable")

def _some_gen():
    yield 1
   
