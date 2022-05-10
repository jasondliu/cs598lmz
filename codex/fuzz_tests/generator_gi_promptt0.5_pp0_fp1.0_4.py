gi = (i for i in ())
# Test gi.gi_code.co_filename

def f():
    return 1

print(f.func_code.co_filename)

# Test gi.gi_code.co_name

def f():
    return 1

print(f.func_code.co_name)

# Test gi.gi_frame.f_globals

def f():
    return 1

print(f.func_code.co_filename)

# Test gi.gi_frame.f_locals

def f():
    return 1

print(f.func_code.co_filename)

# Test gi.gi_frame.f_back

def f():
    return 1

print(f.func_code.co_filename)

# Test gi.gi_frame.f_code

def f():
    return 1

print(f.func_code.co_filename)

# Test gi.gi_frame.f_lineno

def f():
    return 1

print(f.func_code.co_filename)


