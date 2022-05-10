import weakref
# Test weakref.ref(int) and weakref.ref(str)
msg = "weakref.ref(%s) does not raise TypeError"
for T in int, str:
    try:
        weakref.ref(T)
    except TypeError:
        pass
    except:
        print(msg % T.__name__)
def f(): pass
try:
    weakref.ref(f)
except TypeError:
    pass
except:
    print("weakref.ref(function) does not raise TypeError")
m = weakref.ref(f)
try:
    m.foo = 123
except AttributeError:
    pass
else:
    print("weakref.ref assignment to an existing attribute works!")

# Test weakref.proxy
a = []
p = weakref.proxy(a)
if p == a:
    p.append(3)
else:
    print("p != a")
try:
    p.foo = 10
except AttributeError:
    pass
else:
    print("proxy assignment to an existing attribute works!")
def f(): pass
