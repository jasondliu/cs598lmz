import types
types.MethodType(a, 1)

# dynamic attribute creation
class MyClass:
  pass

my_obj = MyClass()
my_obj.foo = 'bar'
my_obj.foo

# dynamic attribute deletion
my_obj.foo
del my_obj.foo
my_obj.foo

# dynamic attribute access
class MyClass:
  pass

my_obj = MyClass()
setattr(my_obj, 'foo', 'bar')
getattr(my_obj, 'foo')

# dynamic attribute access with default value
class MyClass:
  pass

my_obj = MyClass()
getattr(my_obj, 'foo', 'bar')

# dynamic attribute access with default value and callable
class MyClass:
  pass

my_obj = MyClass()
getattr(my_obj, 'foo', lambda: 'bar')()

# dynamic attribute access with default value and callable
class MyClass:
  pass

my_obj = MyClass()
hasattr(my_obj, 'foo')

# dynamic attribute access with default value and
