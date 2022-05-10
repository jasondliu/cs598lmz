import types
types.MethodType(f)
#returns:
MethodType(f, None, None)
</code>
This could be used to implement your idea:
<code>class TypedClass(object):
    def __new__(cls, s):
        cls.name = s
        return cls

class MyClass(object):
    def __init__(self, n):
        self.n = n

def get_class_called(this, s):
    return this.get(s)

def set_class_called(this, s, cls):
    types.MethodType(cls.__call__, None, cls)
    this[s] = cls

fields = {"TypedClass": TypedClass}
fields.__setattr__ = set_class_called
fields.get = get_class_called

f = lambda s: fields[s]
</code>
So, now you can:
<code>f = lambda s: fields[s]
</code>
Which is the same as:
<code>f = lambda s: fields.
