fn = lambda: None
gi = (i for i in ())
fn.__code__ = fn_code
gi[0]
# Tuples don't define __getitem__, so we don't finalize.


class C1(object):
    def __getitem__(self, key):
        if key == 0:
            return sys.exc_info()

fn.__code__.co_consts = [42, (C1(),), 10]

print foo(fn, 7)
# Traceback (most recent call last):
#   File "<string>", line unknown, in ?
#   File "<input>", line 6, in foo
# IndexError: tuple index out of range

class C2(object):
    def __getitem__(self, key):
        if key == 0:
            fn_code.co_consts = [22, "arg", 42]

fn.__code__.co_consts = [42, (C2(),), 10]

print foo(fn, 30)
# 22

class C3(object):
    def __getitem__(self, key):
        if key == 42:
            return 23


