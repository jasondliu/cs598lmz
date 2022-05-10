gi = (i for i in ())
# Test gi.gi_code.co_name
print(gi.gi_code.co_name)

# Test gi.gi_frame
def f():
    yield
fgen = f()
print(fgen.gi_frame.f_lineno)

# Test gi.gi_running
def f():
    print(fgen.gi_running)
    yield
    print(fgen.gi_running)
fgen = f()
print(fgen.gi_running)
next(fgen)
next(fgen)

# Test sys.exc_info
def f():
    print(sys.exc_info())
    try:
        raise ValueError('test')
    except ValueError:
        print(sys.exc_info())
f()

# Test stop
def f():
    print('yield-ing with no value')
    yield
    print('closing with no value')
fgen = f()
next(fgen)
fgen.close()

def f():
    print('yield-ing with value')
    yield 42
    print('closing with
