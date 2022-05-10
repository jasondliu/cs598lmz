import gc, weakref

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print('d["primary"] =', d['primary'])
del a
gc.collect()
print(d['primary'])

# d["primary"] = 10
# 10

# d["primary"] = 10
# Traceback (most recent call last):
#   File "weakref_weakvaluedictionary.py", line 14, in <module>
#     print(d['primary'])
#   File "/usr/local/lib/python3.6/weakref.py", line 117, in __getitem__
#     o = self.data[key]()
# KeyError: 'primary'

# d["primary"] = 10
# Traceback (most recent call last):
#   File "weakref_weakvaluedictionary.py", line 14, in <module>
#     print(d
