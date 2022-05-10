gi = (i for i in ())
# Test gi.gi_code.co_name
print(gi.gi_code.co_name)
print(gi.gi_name)

# Test gi.gi_frame.f_code.co_name
def f():
    gi = (i for i in ())
    print(gi.gi_frame.f_code.co_name)

f()

# Test gi.gi_frame.f_code.co_name
def f():
    gi = (i for i in ())
    print(gi.gi_frame.f_code.co_name)

f()

# Test gi.gi_frame.f_code.co_name
def f():
    gi = (i for i in ())
    print(gi.gi_frame.f_code.co_name)

f()

# Test gi.gi_frame.f_code.co_name
def f():
    gi = (i for i in ())
    print(gi.gi_frame.f_code.co_name)

f()

# Test gi.gi_
