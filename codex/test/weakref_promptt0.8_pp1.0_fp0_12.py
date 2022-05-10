import weakref
# Test weakref.ref by keeping weak references to an object
# and then removing all strong references.


def callback(object_ref):
    print("callback")
    print(object_ref())


weak_ref = weakref.ref(object, callback)
weak_ref2 = weakref.ref(object, callback)
print(weak_ref())
print(weak_ref2())
print(weak_ref is weak_ref2)
del object
print(weak_ref())
print(weak_ref2())
print(weak_ref is weak_ref2)
del weak_ref2
print(weak_ref())
del weak_ref


class ExpensiveObject:
    def f(self):
        print("f()")


def on_finalize(weak_ref):
    print("Called")


instance = ExpensiveObject()
weak_ref = weakref.ref(instance, on_finalize)
print(weak_ref)
print(weak_ref())
print(weak_ref() is instance)

# Check weakref.WeakMethod.
print(f"weakref.WeakMethod")


