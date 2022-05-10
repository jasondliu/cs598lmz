import types
types.MethodType(None, None)

# Test the __doc__ attribute of a built-in function
def f(): pass
f.__doc__

# Test the __dict__ attribute of a built-in class
class C: pass
C.__dict__

# Test the __module__ attribute of a built-in class
class C: pass
C.__module__

# Test the __class__ attribute of a built-in object instance
class C: pass
c = C()
c.__class__

# Test the __bases__ attribute of a built-in class
class C: pass
C.__bases__

# Test the __name__ attribute of a built-in class
class C: pass
C.__name__

# Test the __mro__ attribute of a built-in class
