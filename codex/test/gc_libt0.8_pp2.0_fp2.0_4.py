import gc, weakref
import ctypes

class mylist(list):
    def __init__(self, items=[]):
        print('mylist.__init__')
        super().__init__(items)

    def __del__(self):
        print('mylist.__del__')
        super().__del__()

# mylist.__del__ is not called when the only reference is a weakref
weakhidder = weakref.ref(mylist())
print(weakhidder)
del weakhidder

gc.collect()
print(gc.garbage)
