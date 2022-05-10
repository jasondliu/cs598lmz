fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_get_code_object_from_frame

def f():
    def g():
        return sys._getframe(1)
    return g()

co = f().f_code
assert co.co_name == 'f'
assert co.co_filename == __file__
assert co.co_firstlineno == f.__code__.co_firstlineno

# test_get_code_object_from_frame_with_globals

def f():
    def g():
        return sys._getframe(1)
    return g()

co = f().f_code
assert co.co_name == 'f'
assert co.co_filename == __file__
assert co.co_firstlineno == f.__code__.co_firstlineno

# test_get_code_object_from_frame_with_locals

def f():
    def g():
        return sys._getframe(1)
    return g()

co = f().f_code
assert co.co_name == '
