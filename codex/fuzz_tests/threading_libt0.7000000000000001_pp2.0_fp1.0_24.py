import threading
threading.Thread(target=setup, daemon=True).start()

# %%
import time
time.sleep(5)

# %%
class Test(object):
    def __init__(self, f):
        self.f = f
    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs)
    def __repr__(self):
        return self.f.__repr__()
@Test
def my_func(a):
    return a

# %%
my_func(2)

# %%
my_func

# %%
import types
class Test(object):
    def __init__(self, f):
        self.f = f
    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs)
    def __repr__(self):
        return self.f.__repr__()
    def __get__(self, instance, owner):
        return types.MethodType(self, instance)
class MyClass(object):

