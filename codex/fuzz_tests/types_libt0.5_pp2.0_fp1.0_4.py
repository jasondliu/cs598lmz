import types
types.MethodType(func, obj)
</code>
<code>MethodType</code> is a function that returns a method object.  It takes a function and the object where you want to bind the method to.  You can then assign that method object to an attribute of <code>obj</code>.
<code>obj.func = types.MethodType(func, obj)
</code>

<code>def func(self, x):
    return x

class A(object):
    def __init__(self):
        pass

# create instance
obj = A()

# create method object and assign it to an attribute of obj
obj.func = types.MethodType(func, obj)

# call method
print(obj.func(1))
</code>

