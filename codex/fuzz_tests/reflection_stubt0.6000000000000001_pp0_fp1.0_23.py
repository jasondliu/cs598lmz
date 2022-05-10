fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# test_setattr_class
class C:
    def __setattr__(self, name, value):
        raise NameError(name)

# test_setattr_instance
class D:
    def __setattr__(self, name, value):
        raise NameError(name)

d = D()

# test_getattr_class
class E:
    def __getattr__(self, name):
        raise NameError(name)

# test_getattr_instance
class F:
    def __getattr__(self, name):
        raise NameError(name)

f = F()

# test_delattr_class
class G:
    def __delattr__(self, name):
        raise NameError(name)

# test_delattr_instance
class H:
    def __delattr__(self, name):
        raise NameError(name)

h = H()

# test_getitem_class
class I:
    def __getitem__(self, item):
        raise NameError(item)
