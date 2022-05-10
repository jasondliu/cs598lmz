import weakref
# Test weakref.ref(obj, callback)

class X:
    def __del__(self):
        print("X.__del__")

class Y:
    def __del__(self):
        print("Y.__del__")

def my_callback(x):
    print("my_callback", x)

x = X()
y = Y()

x_ref = weakref.ref(x, my_callback)
y_ref = weakref.ref(y)

del x
del y

print(x_ref())
print(y_ref())
