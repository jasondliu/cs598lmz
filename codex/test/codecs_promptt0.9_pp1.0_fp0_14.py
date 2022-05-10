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
