fn = lambda: None
# Test fn.__code__ will have canonical names
fn.__code__ = co

# test: objects that have __class__ attributes
co.co_names = ["setattr"]
co.co_varnames = ["self"]
fn.__name__ = "test_setattr"
fn.__self__ = fn

class Descriptor:
    def __get__(*args): pass
class C:
    __dict__ = {'a': Descriptor()}
    def __init__(self):
        self.b = Descriptor()
    def __setattr__(self, name, value):
        if name == 'c':
            self.__class__.__dict__[name] = value

co.co_names = ["__init__"]
co.co_varnames = ["self"]
fn.__code__ = co
fn.__name__ = "C.__init__"
fn.__self__ = C.__init__

for obj in [fn, C(), C]:
    test_object(obj)
    assert_equal(obj.__dict__, obj.__
