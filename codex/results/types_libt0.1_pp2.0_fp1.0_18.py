import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

class A(object):
    pass

a = A()
print a.__class__.__name__

print a.__class__.__name__ == 'A'

print a.__class__.__name__ == 'B'

print a.__class__.__name__ == 'C'

print a.__class__.__name__ == 'D'

print a.__class__.__name__ == 'E'

print a.__class__.__name__ == 'F'

print a.__class__.__name__ == 'G'

print a.__class__.__name__ == 'H'

print a.__class__.__name__ == 'I'

print a.__class__.__name__ == 'J'

print a.__class__.__name__ == 'K'

print a.__class__.__name__ == 'L'

print a.__class__.__name__ == 'M'
