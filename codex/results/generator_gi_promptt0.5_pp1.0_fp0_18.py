gi = (i for i in ())
# Test gi.gi_code

def f():
    yield 1

g = f()

if g.gi_code.co_name != 'f':
    print('co_name', g.gi_code.co_name)
    raise Exception

if g.gi_frame.f_code.co_name != 'f':
    print('co_name', g.gi_frame.f_code.co_name)
    raise Exception

if g.gi_frame.f_back:
    print('f_back', g.gi_frame.f_back)
    raise Exception

# Test gi.gi_running

def f():
    yield 1
    yield 2

g = f()

if g.gi_running != False:
    print('gi_running', g.gi_running)
    raise Exception

next(g)

if g.gi_running != True:
    print('gi_running', g.gi_running)
    raise Exception

next(g)

if g.gi_running != False:
    print('gi_running', g.gi
