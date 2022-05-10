import types
types.MethodType(lambda self, x: x.isdigit(), None, str)

# MethodType:
# sig: MethodType(function, instance, class)
# function: function object
# instance: instance object
# class: class object

# python2:
def add_method(cls):
    def method(x):
        print 'method'
    setattr(cls, 'method', method)

class MyClass(object):
    pass

add_method(MyClass)

# python3:
def add_method(cls):
    def method(x):
        print('method')
    setattr(cls, 'method', types.MethodType(method, None, cls))

class MyClass(object):
    pass

add_method(MyClass)

# types.MethodType(function, instance, class)
# function: function object
# instance: instance object
# class: class object

# types.BuiltinMethodType(function, instance, class)
# function: function object
# instance: instance object
# class: class object


