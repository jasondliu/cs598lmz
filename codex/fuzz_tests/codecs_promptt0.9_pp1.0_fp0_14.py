import codecs
# Test codecs.register_error
class MyClass:
    def __init__(self, *args): self.args = args
    def __call__(self, exc):
        raise IOError('call')

try:
    codecs.register_error('test.myclass1', MyClass(1))
except IOError:
    pass
else:
    print 'expected IOError'
try:
    codecs.register_error('', MyClass(1))
except ValueError:
    pass
else:
    print 'expected ValueError'
try:
    codecs.register_error('test.myclass2', '')
except TypeError:
    pass
else:
    print 'expected TypeError'
codecs.register_error('test.myclass3', MyClass)
try:
    x = codecs.lookup_error('test.myclass3')
    if x(1) != ('call', 9, ('test.myclass3', (), 1)):
        print 'expected (call, 9, (test.myclass3, (), 1))'
except IOError:
    print 'expected no
