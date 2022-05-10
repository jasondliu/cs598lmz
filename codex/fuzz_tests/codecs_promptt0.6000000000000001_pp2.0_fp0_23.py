import codecs
# Test codecs.register_error()
with codecs.open(filename, encoding='ascii') as f:
    try:
        f.read()
    except UnicodeDecodeError as e:
        print(e)

def handler(exc):
    if isinstance(exc, UnicodeDecodeError):
        print('UnicodeDecodeError')
        return ('', exc.end)
    raise TypeError(exc)

codecs.register_error('test.ignore', handler)
with codecs.open(filename, encoding='ascii', errors='test.ignore') as f:
    print(f.read())

# Test codecs.lookup_error()
print(codecs.lookup_error('test.ignore'))
print(codecs.lookup_error('test.ignore') is handler)

# Test codecs.strict_errors()
with codecs.open(filename, encoding='ascii', errors='strict') as f:
    try:
        f.read()
    except UnicodeDecodeError as e:
        print(e)

# Test codec
