import io
# Test io.RawIOBase
# Test __init__()
try:
    io.RawIOBase()
except TypeError:
    pass
else:
    print 'FAIL: expected TypeError'

# Test readinto()
try:
    print io.RawIOBase().readinto(buffer('1234567890'))
except IOError as e:
    print 'IOError:', e
except NotImplementedError as e:
    print 'NotImplementedError:', e
else:
    print 'FAIL: expected IOError or NotImplementedError'

# Test write()
try:
    print io.RawIOBase().write('1234567890')
except IOError as e:
    print 'IOError:', e
except NotImplementedError as e:
    print 'NotImplementedError:', e
else:
    print 'FAIL: expected IOError or NotImplementedError'

# Test isatty()
print io.RawIOBase().isatty()

# Test seek()
try:
    print io.RawIOBase().seek(0)
except
