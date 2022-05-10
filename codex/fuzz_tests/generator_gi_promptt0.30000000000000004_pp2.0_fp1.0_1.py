gi = (i for i in ())
# Test gi.gi_code.co_name
print(gi.gi_code.co_name)
# Test gi.gi_frame.f_code.co_name
print(gi.gi_frame.f_code.co_name)

def g():
    yield 1

# Test g.gi_code.co_name
print(g().gi_code.co_name)
# Test g.gi_frame.f_code.co_name
print(g().gi_frame.f_code.co_name)

# Test g.gi_code.co_name
print((lambda: (yield 1)).gi_code.co_name)
# Test g.gi_frame.f_code.co_name
print((lambda: (yield 1)).gi_frame.f_code.co_name)

# Test g.gi_code.co_name
print((lambda: (yield from range(1))).gi_code.co_name)
# Test g.gi_frame.f_code.co_name
print((lambda: (yield from range(1))).gi_
