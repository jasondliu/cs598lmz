import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()

ERR = (TypeError, ValueError, EnvironmentError)

assert isinstance(a, bytes_type), type(a)
assert a == bytes(1), a

# All following operations should raise EnvironmentError
ope
