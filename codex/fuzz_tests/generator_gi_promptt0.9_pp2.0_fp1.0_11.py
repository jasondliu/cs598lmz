gi = (i for i in ())
# Test gi.gi_code / gi.gi_frame
gi.gi_code, gi.gi_frame

gi = type(gi)(i for i in ())
# Test gi.gi_frame
gi.gi_frame

def gen():
    for i in range(5):
        yield i

# should not raise exception
g = gen()
gen_send(g, None)

# Test other methods on generators
test_generator_methods()

# Test generator send method on done generator
try:
    gen_send(g, None)
    raise TestFailed
except StopIteration:
    pass

# Test generator send method on non-generator
try:
    gen_send(5, None)
    raise TestFailed
except TypeError:
    pass

check_send(None)

def gen_except():
    yield 1
    try:
        yield
    except:
        yield 2
    raise StopIteration

check_send(gen_except())
check_send(gen_except())

def gen_finally():
    yield 1
    try
