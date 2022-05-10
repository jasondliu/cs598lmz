import codecs
# Test codecs.register_error

def lookuperror(errorname, logname='<logfile>'):
    print(logname, errorname)
    return 'xxx', 0

codecs.register_error('test.lookuperror', lookuperror)

assert 'test.lookuperror' in codecs.lookup_error('test.lookuperror')
assert lookuperror in codecs.lookup_error('test.lookuperror')
print('registered error handler')

assert 'test.lookuperror' not in codecs.lookup_error('test.lookuperror2')
print('lookup by wrong name')

assert lookuperror not in codecs.lookup_error('test.lookuperror2')
print('lookup by wrong name')

codecs.register_error('test.lookuperror2', lookuperror)
assert lookuperror in codecs.lookup_error('test.lookuperror2')
print('lookup by right name')


def ignoreerror(errorname, logname='<logfile>'):
    print(
