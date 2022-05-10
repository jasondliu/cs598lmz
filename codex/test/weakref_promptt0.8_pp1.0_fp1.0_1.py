import weakref
# Test weakref.ref() on a builtin function

def f():
    return 'hello world'

r = weakref.ref(f)

print(r())
print(r() is f)

del f
unittest.main()
