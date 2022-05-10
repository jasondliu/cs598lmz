fn = lambda: None
# Test fn.__code__ is None

def module_fn():
    pass
module_fn.__code__ = None

# Test fn.__code__ is a function

def module_fn_2():
    pass
module_fn_2.__code__ = module_fn

# Test fn.__code__ is a code object with no filename
module_fn_3.__code__.co_filename = None

# Test fn.__code__ is a code object with a filename

def module_fn_3():
    pass
module_fn_3.__code__.co_filename = __file__


class TestClass:
    def __getattr__(self, attr):
        return None
    def __repr__(self):
        return ""

# Test __module__ is None

class_fn = TestClass()
class_fn.__call__ = lambda: None
class_fn.__call__.__code__ = None

class_fn.__code__ = module_fn

class_fn.__call__.__code__ = module_fn_3.__code__
