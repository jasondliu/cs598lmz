import weakref
# Test weakref.ref(f)():
def f():
    print('f')
r = weakref.ref(f)
# r()
s = r()
print(s)
# del f
# print(r())
# r()()
