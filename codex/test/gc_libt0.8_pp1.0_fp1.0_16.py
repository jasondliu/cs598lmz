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
