import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakref callbacks.
#
# This test has been added to test the new feature of Python 2.0,
# namely to call tp_clear for objects involved in a gc.collect().


class MyBase(object):
    # Simulate a base class with a __del__ method.
    def __del__(self):
        pass


class MyObject(MyBase):
    # A count variable shared by all instances.
    total_count = 0

    def __init__(self):
        MyObject.total_count = MyObject.total_count + 1
        self.my_data = range(100)

    def __del__(self):
        MyObject.total_count = MyObject.total_count - 1

    def get_total_count():
        return MyObject.total_count
    get_total_count = staticmethod(get_total_count)


def callback(w):
    print("callback", w)
    # This callback is called for each object involved in the gc.collect()
    # below.  The objects should be all alive.
   
