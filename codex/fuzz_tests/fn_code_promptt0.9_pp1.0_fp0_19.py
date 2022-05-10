fn = lambda: None
# Test fn.__code__.co_firstlineno

def foo():
    print "bla"

foo.__code__.co_firstlineno
def foo2():
   pass

foo2.__code__.co_firstlineno
foo2.func_code.co_firstlineno
foo2.__code__
foo2.__code__.co_varnames
foo2.__code__.co_argcount

foo3 = lambda: None
import inspect
inspect.getsourcelines(foo3)
inspect.getsourcelines(foo)
foo4 = lambda x, y : x + y
inspect.getsourcelines(foo4)
foo.__code__.co_argcount
foo.__code__.co_varnames
# Can manage attributes in module

print sys.getdlopenflags()
sys.setdlopenflags(os.RTLD_NOW | os.RTLD_GLOBAL)
print sys.getdlopenflags()
sys.setdlopenflags(os.RTLD_LAZY | os.RTLD_GLOBAL)
print sys
