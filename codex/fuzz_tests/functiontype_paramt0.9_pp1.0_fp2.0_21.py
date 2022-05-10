from types import FunctionType
list(FunctionType(lambda f: f, lambda f: f).__globals__)


### One of the things that we can do with this __globals__ attribute is dynamically add elements to global namespace of a function. The following is possible:
FunctionType(lambda f: f, {}).__call__ = True

### If we now had a custom __call__ method and it used something from the global namespace then that would give us an opportunity to influence the behavior of the function. The following is a straightforward example of what we can do:
def func(*args, **kw):
    return '__call__' in func.__globals__

### Now all that we need for our exploit is a way to pass an object with custom __call__ method to our attacker's code. Luckily it is pretty simple, as following will work:
FunctionType(lambda f: f, {})()
