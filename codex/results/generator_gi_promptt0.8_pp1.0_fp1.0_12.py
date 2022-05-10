gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    pass
else:
    print('AttributeError expected')

# Must not store the exception when we don't use it, because the exception
# object has a reference back to the generator which could cause problems
# when the generator is being destroyed.
def gen():
    try:
        yield
    except:
        pass
g = gen()
g.send(None)
g.throw(RuntimeError)

# Set gi_code without gi_frame
gi = (i for i in ())
gi.gi_code = (lambda:1).__code__
print(gi.gi_code is (lambda:2).__code__)

# Only code objects have a co_code attribute
class C:
    pass
try:
    gi = (i for i in ()).gi_code = C()
except TypeError:
    pass
else:
    print('TypeError expected')

gi = (i for i in ()).send
print(gi(42) == 42)

# Verify we can set gi
