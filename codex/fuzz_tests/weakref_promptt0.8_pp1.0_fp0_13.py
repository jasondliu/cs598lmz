import weakref
# Test weakref.ref(obj) -- reference to an object

#Create a reference to an object
a = weakref.ref(object())

#Create a weakref to an object
b = weakref.ref(a)

#Create a weakref to an object
c = weakref.ref(b)

print("a: ", a)
print("b: ", b)
print("c: ", c)
print("c is a: ", c is a)
print("c() is a(): ", c() is a())
print("c() is b: ", c() is b)
print("c()() is a(): ", c()() is a())
print("c()() is c: ", c()() is c)
print("a(): ", a())
print("b(): ", b())
print("c(): ", c())
print("c()(): ", c()())


print("---------")
# Create a reference to an object
a = weakref.ref(object())

#Create a weakref to an object
b = weakref.ref(a)

#Create a weakref to an object
c =
