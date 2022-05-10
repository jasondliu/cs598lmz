import weakref
# Test weakref.ref()

class T:
    pass

t = T()

# ref()
print(weakref.ref(t))

# ref(obj, callback)
def callback(obj):
    print("callback:", obj)

print(weakref.ref(t, callback))

# ref(obj, callback, value)
def callback(obj):
    print("callback:", obj)

print(weakref.ref(t, callback, "value"))

# ref(obj, callback, value, callback2)
def callback(obj):
    print("callback:", obj)

def callback2(obj):
    print("callback2:", obj)

print(weakref.ref(t, callback, "value", callback2))

# ref(obj, callback, value, callback2, value2)
def callback(obj):
    print("callback:", obj)

def callback2(obj):
    print("callback2:", obj)

print(weakref.ref(t, callback, "value", callback2, "value2"))

# ref(obj,
