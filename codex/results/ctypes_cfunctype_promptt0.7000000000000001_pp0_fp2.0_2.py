import ctypes
# Test ctypes.CFUNCTYPE

def get_callback(f):
    if not isinstance(f, type(get_callback)):
        f = get_callback(f)
    return f

def get_callback_class(f):
    if not isinstance(f, type(get_callback_class)):
        f = get_callback_class(f)
    return f

def get_callback_instance(f):
    if not isinstance(f, type(get_callback_class)):
        f = get_callback_instance(f)
    return f

def callback(arg):
    print 'callback(%r)' % (arg,)
    return arg + 1

class Foo:
    def __init__(self):
        self.x = 3

    def callback(self, arg):
        print 'Foo.callback(%r)' % (arg,)
        return arg + self.x

class Bar:
    def __init__(self):
        self.x = 5

    def callback(self, arg):
        print 'Bar.callback(%r)' % (arg,)

