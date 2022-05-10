fn = lambda: None
gi = (i for i in ())
fn.__code__ = Enum

gi.gi_code = Enum
def bar(x: object, y: object, z: object = ...) -> object: pass

bar.__code__ = Enum


def foo(x: object, y: object, z: object = ...) -> object: pass


bar(1, 2)
bar(a=1, b=2)
bar(1, 2, 3)
bar(1, 2, 3, a=1)
foo(1, 2)
foo(1, a=1, y=2)
foo(1, 2, 3)
foo(1, 2, 3, x=1)
foo(1, 2, 3, z=1)
bar(x=1, y=2)
bar(1, 2, z=3)
bar(1, y=2, x=1)
foo(x=1, y=2)
foo(1, y=2, z=3)
foo(1, 2, z=3)
bar(1, *(2,))
bar(z=1, *(2,),
