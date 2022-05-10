import weakref
# Test weakref.ref to call lambda

# Write your code here
#x = weakref.ref(lambda: None)

def f1():
   print("f1")

x = weakref.ref(f1)
x()

import random
import weakref

# Write your code here
#x = weakref.ref(lambda: print(random.randint(1, 100)))
#print(x)

import random
import weakref

# Write your code here
x = weakref.WeakKeyDictionary()
x.update({lambda: print(random.randint(1, 100)): 'test'})

import weakref

# Write your code here
a = weakref.WeakKeyDictionary()
a.update({1: 'test'})
a[1]

import weakref

# Write your code here
a = weakref.WeakValueDictionary()
a.update({1: 1})
a[1]

import weakref

# Write your code here
a = weakref.WeakSet()
b = weakref.WeakKeyDictionary()
c = weak
