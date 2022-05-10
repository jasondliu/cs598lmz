gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code)

def foo():
    yield
gen_foo = foo()
# Test gen_foo.gi_code
print(gen_foo.gi_code)
