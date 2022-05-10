import codecs
# Test codecs.register_error
try:
    codecs.register_error('test1', codecs.lookup_error('replace'))
except TypeError:
    print('SKIP')
    raise SystemExit

# Test codecs.register_error
try:
    codecs.register_error('test2', codecs.lookup_error('replace'))
except TypeError:
    print('SKIP')
    raise SystemExit

# Test codecs.register_error
try:
    codecs.register_error('test3', codecs.lookup_error('replace'))
except TypeError:
    print('SKIP')
    raise SystemExit

# Test codecs.register_error
try:
    codecs.register_error('test4', codecs.lookup_error('replace'))
except TypeError:
    print('SKIP')
    raise SystemExit

# Test codecs.register_error
try:
    codecs.register_error('test5', codecs.lookup_error('replace'))
except TypeError:
    print('SKIP')
    raise SystemExit
