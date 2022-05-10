import gc, weakref

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print('before del a')
for key, value in d.items():
    print(key, value)
del a
print('after del a')
for key, value in d.items():
    print(key, value)
print('collecting')
gc.collect()
print('after collecting')
for key, value in d.items():
    print(key, value)

# before del a
# primary 10
# after del a
# primary 10
# collecting
# after collecting
# primary None
