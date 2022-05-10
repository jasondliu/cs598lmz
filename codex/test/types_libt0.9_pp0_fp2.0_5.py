import types
types.MethodType(lambda self: self.c == 'C', o)
o.m()

# and using __get__
types.MethodType(lambda self: self.c == 'C', o.__dict__, o)
o.m()

