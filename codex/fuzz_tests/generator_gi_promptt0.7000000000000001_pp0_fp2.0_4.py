gi = (i for i in ())
# Test gi.gi_code.co_flags
print(next(gi))

# Test gi.gi_frame.f_code.co_flags
print(gi.gi_frame.f_code.co_flags)

# Test gi.gi_frame.f_lineno
print(gi.gi_frame.f_lineno)


# Test f.f_code.co_flags
def f():
    print("")
    try:
        print("")
    except:
        pass
    try:
        print("")
    finally:
        print("")
    print("")
    print("")
    return 0

print(f.__code__.co_flags)

# Test f.f_lineno
print(f.__code__.co_firstlineno)

# Test f.f_lasti
try:
    pass
except:
    pass

# Test f.f_trace

def f():
    print("")

def g():
    f()

def h():
    g()

def i():
    h()

i
