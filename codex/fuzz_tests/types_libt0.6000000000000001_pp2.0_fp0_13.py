import types
types.MethodType(func, obj)  # create a bound method from `func`

# unbound methods can be converted to functions using `__func__`
unbound.__func__(obj, *args)  # call the underlying function

# bound methods can be converted to functions using `__func__`
unbound.__func__(obj, *args)  # call the underlying function
```

```py
class Test(object):
    def __init__(self):
        self.name = 'name'

    def test(self):
        print self.name

test_obj = Test()

test_func = test_obj.test  # unbound method
test_func.__class__  # <type 'instancemethod'>
test_func(test_obj)  # name

test_func = test_obj.test.__func__  # bound method
test_func.__class__  # <type 'function'>
test_func(test_obj)  # name

test_func = Test.test  # unbound method
test_func.__class__  #
