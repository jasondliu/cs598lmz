import ctypes
ctypes.cast(100, ctypes.py_object)

# dunder method

class A:
    def __getitem__(self, item):
        return item

a = A()
#print(a[1])
a[1]

# dunder function

class A:
    def __call__(self, *args, **kwargs):
        print(args, kwargs)

a = A()
a(1, 2, 3, 4)

print(max([1, 2, 3, 4]))
print(min([1, 2, 3, 4]))

#print(max([1, 2, 3, 4], key=lambda x: -x))

print(max(1, 2, 3, 4))
print(min(1, 2, 3, 4))

print(max(1, 2, 3, 4, key=lambda x: -x))

# isinstance

print(isinstance(100, int))
print(isinstance(100, float))
print(isinstance(100, (int, float)))

# issubclass
