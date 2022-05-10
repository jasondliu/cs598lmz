fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

m = memoryview(fn)
print(sorted(m.format))

print(m.ndim)
print(m.shape)
print(m.strides)
print(m.suboffsets)

# issue6567
class Foo(object):
    def __array__(self):
        return [1,2,3]

f = Foo()
m = memoryview(f)
print(m.ndim)
print(m.shape)
print(m.strides)
print(m.suboffsets)

print(memoryview(memoryview(b"abcd")).tobytes())

print(memoryview(memoryview(memoryview(b"abcd")).tobytes()).tobytes())

print(memoryview(memoryview(memoryview(memoryview(b"abcd")).tobytes()).tobytes()).tobytes())

print(memoryview(memoryview(memoryview(memoryview(memoryview(b"abcd")).tobytes()).tobytes()).tobytes()).
