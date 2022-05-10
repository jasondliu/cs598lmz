gi = (i for i in ())
# Test gi.gi_code.co_flags

def f():
    pass

print f.func_code.co_flags


# Test code.co_consts

def f():
    return 1

print f.func_code.co_consts, f.func_code.co_consts[0]

# Test code.co_varnames

print f.func_code.co_varnames

# Test code.co_cellvars

def make_adder(n):
    def adder(x):
        return x + n
    return adder

print make_adder(7).func_code.co_cellvars


# Test code.co_freevars

def make_adder(n):
    if n == 0:
        return lambda x: x
    else:
        return lambda x: x + make_adder(n-1)(x)

print make_adder(7).func_code.co_freevars


# Test code.co_filename

print f.func_code.co_filename


# Test code.co_
