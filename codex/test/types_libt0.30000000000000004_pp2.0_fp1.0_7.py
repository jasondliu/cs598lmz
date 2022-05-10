import types
types.MethodType(lambda self: None, None, Dummy)

# __dict__ assignment
class Dummy:
    pass

Dummy.attr = 1
Dummy.__dict__
Dummy.__dict__ = {'bar': 2}
Dummy.bar
Dummy.__dict__ = {'__dict__': 3}
Dummy.__dict__

# __dict__ deletion
class Dummy:
    pass

Dummy.attr = 1
del Dummy.attr
Dummy.__dict__
del Dummy.__dict__
Dummy.__dict__

# __dict__ shadowing
class Dummy:
    pass

Dummy.__dict__ = {'__dict__': 1}
Dummy.__dict__

# __dict__ shadowing with a property
class Dummy:
    @property
    def __dict__(self):
        return {'__dict__': 1}

Dummy.__dict__

