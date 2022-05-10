gi = (i for i in ())
# Test gi.gi_code is the code of the genexp
if gi.gi_code.co_code is not gi.__code__.co_code:
    print('co_code should be the same for the generator and its code object!')

# Test gi.gi_frame is the frame of the genexp
if gi.gi_frame.f_code.co_name != gi.__name__:
    print('co_name should be the same for the generator and its code object!')

# Test gi.gi_running.
def test_genexp(i):
    return [i for i in ()]

gi = test_genexp(3)
if gi.gi_running:
    print('gi_running should be set to false when generator is created!')


# Test passing generator instances as argument to exec
def test_exec(arg):
    exec(arg)

gi = test_genexp(3)
test_exec(gi)

# Test passing generator instances as argument to list
gi = test_genexp(2)
try:
    l = list(gi
