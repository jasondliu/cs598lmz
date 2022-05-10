import weakref
# Test weakref.ref(Test) is weakref.ReferenceType
print(type(weakref.ref(Test)))
# weakref.ref(Test) is weakref.ReferenceType
print(isinstance(weakref.ref(Test), weakref.ReferenceType))
