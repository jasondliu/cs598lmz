from types import FunctionType
list(FunctionType(lambda x:x**2, globals(), "f")(3).items())

#Output:
[('__name__', 'f'), ('__qualname__', 'f'), ('__module__', '__main__')]


#3. You can also add attributes to instance methods.

def baz(self):
    pass
def bar(self):
    pass
class Foo():
    pass

#instance method
Foo.foo_meth = baz
Foo.bar_meth = bar
foo_obj = Foo()

#Each instance of Foo will have an attribute .foo_meth pointing to the baz function.
#foo_obj.foo_meth() simply calls Foo.foo_meth(foo_obj)
Foo.__dict__
#Output:
mappingproxy({
 '__module__': '__main__', 
 '__dict__': <attribute '__dict__' of 'Foo' objects>, 
 '__weakref__': <attribute '__weakref__' of 'Foo' objects>, 
 '__doc__': None, 
