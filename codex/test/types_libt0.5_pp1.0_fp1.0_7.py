import types
types.SimpleNamespace(a=1)

class Namespace(dict):
    def __getattr__(self, key):
        return self[key]

ns = Namespace(a=1)
ns.a

ns['a']

ns.b = 2
ns['b']

ns.update(b=3, c=4)
ns

ns.update(dict(d=5, e=6))
ns

ns.update(d=7, e=8)
ns

ns.update(**dict(d=9, e=10))
ns

class Namespace(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__dict__ = self

ns = Namespace(a=1)
ns.a

ns['a']

ns.b = 2
ns['b']

ns.update(b=3, c=4)
ns

ns.update(dict(d=5, e=6))
ns

