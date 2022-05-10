import types
types.new_class("A",
        tuple("abcde".split()) + ("__basicfields__", "__initfields__"),
        (A, ),
        {"__fields__": tuple("abc".split())})
types.new_class("B",
        tuple("fghij".split()) + ("__basicfields__", "__initfields__"),
        (B, ),
        {"__fields__": tuple("fgh".split()) + ("a", )})

class C(object):
    __basicfields__ = tuple("klm".split())
    __initfields__ = tuple("klm".split())

class D(object):
    __basicfields__ = tuple("nopqr".split())
    __initfields__ = tuple("mnop".split())
    __fields__ = tuple("rmnp".split())

class E(A, B, C, D):
    __fields__ = tuple("abcdefghijklmnopqr".split())
    def __init__(self, *args, **kwargs):
        A.__init__(self, *args, **
