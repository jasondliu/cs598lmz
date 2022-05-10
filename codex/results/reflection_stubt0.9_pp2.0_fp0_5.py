fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
output = None
try:
    exec("f()")
except Exception as e:
    output = e

output

output.args  # i.e. ("co_code must be a string or compiled code object",)
type(output)  # TypeError

class ReadOnlyClass:
    __slots__ = tuple()
read_only_class = ReadOnlyClass()


try:
    read_only_class.a = 2
except Exception as e:
    output = e
type(output)
output.args

class Bar(Exception):
    pass


raise Bar('test')
def foo():
    def raise_foo():
        raise Bar('test')
    try:
        raise_foo()
    except Exception as e:
        return e.args[0]

foo()


class __Foo:
    def __repr__(self):
        raise RuntimeError('foobar')
# Foo()
class Foo:
    def __init__(self):
        self.__class__ = __Foo

Foo()
# class Foo(
