fn = lambda: None
# Test fn.__code__
setattr(fn, '__code__', code)

# In Python 3.x, adding an attribute in a class definition creates a class attribute
# Class attribute is inherited by all instances of the class, and any changes to the class
# attribute are reflected in all instances that inherit from the class
# In Python 2.x, attributes are assigned to instances only
# Class attributes must be set in the class body

class Test(object):
    class_attr = 'my class attribute'

    def __init__(self):
        self.instance_attr = 'my instance attribute'

t = Test()
print(t.class_attr)
print(t.instance_attr)
# In Python 3.x, adding an attribute in a class definition creates a class attribute
# Class attribute is inherited by all instances of the class, and any changes to the class
# attribute are reflected in all instances that inherit from the class
# In Python 2.x, attributes are assigned to instances only
# Class attributes must be set in the class body

class Test(object):
    class_attr = 'my class attribute'

    def __init__(
