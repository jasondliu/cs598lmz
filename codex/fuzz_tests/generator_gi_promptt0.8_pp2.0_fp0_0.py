gi = (i for i in ())
# Test gi.gi_code.co_filename
gi = (i + 1 for i in ())
# Test gi.gi_code.co_name
gi = (i for i in ())

# Test closure
def func(a):
    return lambda b: b + a
func(1)(2)

# Test nested loop
for i in range(1):
    for j in range(2):
        pass

# Test kwargs
def func(a, b, **kwargs):
    pass
func(1, {}, a=1, b=2)
