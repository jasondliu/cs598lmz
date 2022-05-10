gi = (i for i in ())
# Test gi.gi_code.co_varnames
print(gi.gi_code.co_varnames)
# Test gi.gi_code.co_name
print(gi.gi_code.co_name)
# Test gi.gi_frame.f_code.co_name
print(gi.gi_frame.f_code.co_name)
# Test gi.gi_frame.f_code.co_varnames
print(gi.gi_frame.f_code.co_varnames)

print(sys.exc_info())

a = 10
b = 20
print(a, b)
a, b = b, a
print(a, b)

# Test a generator that yields twice
def twice(value):
    yield value
    yield value

# Test a generator that yields once
def once(value):
    yield value

# Test a generator that yields nothing
def nothing():
    pass

print(list(twice(1)))
print(list(once(1)))
print(list(nothing()))

# Test a generator that yields one
