import gc, weakref, sys

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)                   # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a            # does not create a reference
d['secondary'] = a          # does not create a reference
print(d['primary'])         # fetch the object if it is still alive
del a                       # remove the one reference
gc.collect()                # run garbage collection right away
print(d['primary'])         # entry was automatically removed

# Output:
# 10
# 10
# Traceback (most recent call last):
#   File "weakref_weakvaluedictionary.py", line 17, in <module>
#     print d['primary']
#   File "/usr/lib/python3.6/weakref.py", line 117, in __getitem__
#     o = self.data[key]()
# KeyError: 'primary'

# You can use WeakValueD
