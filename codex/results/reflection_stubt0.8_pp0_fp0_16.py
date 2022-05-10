fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'x'

try:
    __import__(fn.__name__)
except ValueError as e:
    assert e.args[0].startswith("code object passed to exec")


def fn():
    pass


try:
    exec(fn)
except ValueError as e:
    assert e.args[0].startswith("code object passed to exec")

try:
    exec(fn, fn.__code__.co_names)
except ValueError as e:
    assert e.args[0].startswith("code object passed to exec")

try:
    exec(1)
except TypeError as e:
    assert e.args[0].startswith("exec: arg 1 must be")

try:
    exec({'a': 1}, 1)
except TypeError as e:
    assert e.args[0].startswith("exec: arg 2 must be")

try:
    exec({'a': 1}, {'a': 1}, 1)
except TypeError as e:
