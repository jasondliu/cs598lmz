import weakref
# Test weakref.ref()

class C:
    pass

r = weakref.ref(C())
print(r(), r())

c = C()
r = weakref.ref(c)
print(r(), r())

print('del c')
del c
print(r(), r())

if __name__ == '__main__':
    import support
    support.run_unittest(__name__)
