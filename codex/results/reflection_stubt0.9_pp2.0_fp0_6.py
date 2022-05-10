fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code


class Foo:
    pass


class Bar:

    def __getattr__(self, attr):
        pass

    def __setattr__(self, attr, val):
        pass


class FooWithMeta(type):
    pass


class MyInt(int):
    pass


class NewStyleClass(object):
    pass


class WrapIntSpecial(int):
    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return False


class WrapFloatSpecial(float):
    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return False


class WrapIntNoSpecial(int):
    pass


class WrapFloatNoSpecial(float):
    pass

import gc
gc.disable()


def test_missing_cpy_file():

    class C(object):
        pass

    schema = bdb.schema.Schema(C)
    schema.configure(store_cpy_files=3)
