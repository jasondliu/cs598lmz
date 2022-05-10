import weakref
# Test weakref.ref() of a UserWarning
try:
    UserWarning()
except NameError:
    print('SKIP')
    raise SystemExit

class DerivedUserWarning(UserWarning):

    def __init__(self, a):
        Exception.__init__(self, a)

o = DerivedUserWarning(5)
w = weakref.ref(o)
print(type(w))
print(type(w()) is DerivedUserWarning)
print(w().args)
print(w())
print(w() is o)
