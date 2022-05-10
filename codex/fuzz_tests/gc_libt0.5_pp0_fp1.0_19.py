import gc, weakref

class A:
    def __del__(self):
        print('A.__del__')

a = A()
r = weakref.ref(a)
print('a:', a)
print('ref:', r)
print('r():', r())

del a
print('ref:', r)
print('r():', r())

gc.collect()
print('ref:', r)
print('r():', r())

# A.__del__
# a: <__main__.A object at 0x10e868b00>
# ref: <weakref at 0x10e868b48; to 'A' at 0x10e868b00>
# r(): <__main__.A object at 0x10e868b00>
# ref: <weakref at 0x10e868b48; dead>
# r(): None
# ref: <weakref at 0x10e868b48; dead>
# r(): None
