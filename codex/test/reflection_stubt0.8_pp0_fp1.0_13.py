fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = "foo"
fn.__module__ = "bar"

class Foo:
    def __getattr__(self, name):
        raise AttributeError("flabbergast")

# Try loading builtins and sys
orig_modules = [__name__]
globals()["_name"] = globals()["__name__"]
globals()["_name_"] = globals()["__name__"]
del globals()["__name__"]
for i in range(3):
    try:
        import _name
        orig_modules.append("_name")
    except ImportError:
        pass
    try:
        import _name_
        orig_modules.append("_name_")
    except ImportError:
        pass
    try:
        import __name__
    except ImportError:
        pass
    else:
        orig_modules.append("__name__")
    globals()["__name__"] = "foo"
del globals()["_name"]
