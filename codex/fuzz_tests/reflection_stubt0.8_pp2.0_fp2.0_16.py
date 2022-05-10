fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(lambda: None)()
fn.__code__.co_varnames = gi.gi_code.co_varnames = ()
fn.__code__.co_argcount = gi.gi_code.co_argcount = 0
fn.__code__.co_cellvars = gi.gi_code.co_cellvars = ()

# create an empty module
module = imp.new_module("module")
module.__dict__["__file__"] = "<test>"

# define fib in the module
exec("""def fib(n):
    if n <= 1: return n
    return fib(n - 1) + fib(n - 2)""", module.__dict__)


def traceit(frame, event, arg):
    if event == "line":
        print("{}:{}".format(frame.f_code.co_filename, frame.f_lineno))
    return traceit


def test_del():
    settrace(traceit)
    del sys.settrace
    settrace
