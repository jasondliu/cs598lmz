gi = (i for i in ())
# Test gi.gi_code is not None
try:
    gi.gi_code
except AttributeError:
    print "SKIP"
    raise SystemExit

class A:
    def __iter__(self):
        return (i for i in ())

for x in A():
    pass

# Test that genexp is not a generator
print type(A()).__name__

# Test that generator methods can't be called on genexp
try:
    (i for i in ()).send(1)
except AttributeError:
    print "GenExpError"
