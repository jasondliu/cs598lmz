fn = lambda: None
# Test fn.__code__
try:
    fn.__code__
except (NameError, AttributeError):
    # Python 2.6 or earlier
    import functools
    import new
    def make_closure(env, fn, *args):
        return functools.partial(fn, *args)
    def set_closure(closure, env):
        # This will fail if the closure uses the environment
        pass
    def make_cell(value):
        return None
    def make_function(env, code, closure):
        return new.function(code, env)
else:
    # Python 2.7 or later
    def make_closure(env, fn, *args):
        return fn.__closure__[0].cell_contents
    def set_closure(closure, env):
        closure.__closure__ = (make_cell(env),)
    def make_cell(value):
        return (lambda: value).__closure__[0]
    def make_function(env, code, closure):
        return types.FunctionType(code, env, None, None, closure)

def
