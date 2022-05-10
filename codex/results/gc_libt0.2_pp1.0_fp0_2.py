import gc, weakref

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])
del a
gc.collect()
print(d['primary'])

# 10
# 10
# Traceback (most recent call last):
#   File "weakref_weakvaluedictionary.py", line 15, in <module>
#     print(d['primary'])
# KeyError: 'primary'
