import weakref
# Test weakref.ref() on a list subclass

class X(list):
    pass

class Y(X):
    pass

class Z(Y):
    pass

class C(object):
    pass

x = X()
y = Y()
z = Z()
c = C()

x.append(y)
y.append(z)
y.append(c)

x_r = weakref.ref(x)
y_r = weakref.ref(y)
z_r = weakref.ref(z)
c_r = weakref.ref(c)

print(x_r())
print(y_r())
print(z_r())
print(c_r())

del x
del y
del z
del c

print(x_r())
print(y_r())
print(z_r())
print(c_r())
