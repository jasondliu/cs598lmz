import types
types.MethodType(a, object())

# now you can see that it's possible to make a method for any type
# (for example, for list)
# but we can't assign it to the list itself
# because it's type is not mutable
l = list()
l.append = a
l.append(1)

# it's possible to add any method for the type
# for example, let's add a method for the int
# that will increase the number by 1
def add_one(self):
    return self + 1


int.add_one = add_one

# now we can use it
print(1.add_one())

# we can't add a method to the type directly
# because it's type is not mutable
# but we can add it to the class itself
# that will allow us to use it in the derived classes
class C:
    pass


C.add_one = add_one

# now we can use it in the derived class
class D(C):
    pass


print(D().add_one())

# we can't assign a
