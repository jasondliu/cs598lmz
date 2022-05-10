gi = (i for i in ())
# Test gi.gi_code


def f(n):
    while n > 0:
        yield n
        n -= 1
    yield 0
    return
    yield 1  # unreachable
g = f(10)
g.gi_code = 1


def f(n):
    while n > 0:
        yield n
        n -= 1
    yield 0
    raise StopIteration()
    yield 1  # unreachable
# Test gi.gi_frame and gi.gi_running
g = f(10)
g.gi_frame = 1
g.gi_running = 1


def f(n):
    while n > 0:
        yield n
        n -= 1
    yield 0
    return
    yield 1  # unreachable
# Test gi.gi_frame and gi.gi_running
g = f(10)
g.gi_frame.f_trace = 1
g.gi_running.f_trace = 1


def f(y, li):
    while y:
        yield y
        li.append(y)
        y -= 1
for k in list
