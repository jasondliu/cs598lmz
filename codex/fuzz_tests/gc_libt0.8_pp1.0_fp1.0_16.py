import gc, weakref, sys

# a = [i for i in range(0, 1000000)]
a = list(range(1000000))
print(a[:5])
print(sys.getsizeof(a))

b = weakref.WeakValueDictionary()

def callback(value):
    print('value is gone! value => {}'.format(value))
    print(sys.getsizeof(b))

# b['a'] = a
b['a'] = weakref.ref(a, callback)
print(b['a'][:5])
# del a
a = None
gc.collect()
print(b['a'])

# b['a'][0] = 100
b['a'][0] = 100
print('a is now => {}'.format(a))
print(b['a'])
print(b['a'][:5])
print(b['a'][0])
