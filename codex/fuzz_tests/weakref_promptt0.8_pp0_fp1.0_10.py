import weakref
# Test weakref.ref() with a callable
import _weakref

class MyRef(weakref.ref):
    def __call__(self):
        return self.__callobj__(self)


class MyObj(object):
    def __init__(self, x):
        self.x = x

    def my_callable(self, ref):
        return 'hello there'


obj1 = MyObj(1)
r1 = MyRef(obj1, obj1.my_callable)
assert r1() == 'hello there'
obj1 = None
assert r1() == 'hello there'

# Test weakref.ref() with native objects

def my_callback(object):
    return None

def create_ref(obj):
    return weakref.ref(obj, my_callback)

class MyNewObj(object):
    def __init__(self, x):
        self.x = x

new_obj = MyNewObj(1)
new_ref = weakref.ref(new_obj)
assert new_ref() is new_obj
assert new_
