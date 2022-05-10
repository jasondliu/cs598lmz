import weakref
# Test weakref.ref(x).get_weakref_type() implicitly calls type(x)._add_items()

class Client:

    def _add_items(self, generator):
        for item in generator:
            self.append(item)

class MyClass:
    pass

ref = weakref.ref(Client())

class MyClass(MyClass, Client):
    pass

t = MyClass()

l = [i, i]

t._add_items(l)

print(ref)
print(ref())
print(ref.get_weakref_type())
