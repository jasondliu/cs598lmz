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
del gc.garbage[-1]
gc.collect()
print(gc.garbage)

print('*' * 40)

# mylist.__del__ is called when the reference is a weakref and a normal reference
obj = mylist()
weakhidder = weakref.ref(obj)
print(weakhidder)
del weakhidder
del obj
gc.collect()
print(gc.garbage)

print('*' * 40)

# mylist.__del
