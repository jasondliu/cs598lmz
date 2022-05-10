gi = (i for i in ())
# Test gi.gi_code
try:
    compile('''\
def f():
    a = 1
    yield 1
    b = 2
    yield 2
    c = 3
    yield 3
''', '', 'exec')
except SyntaxError:
    pass
# Try gi.gi_name
try:
    (lambda: (yield))()
except SyntaxError:
    pass
# Try gi.gi_frame and stack level
def gen():
    yield 1
gi = gen()
next(gi)
# Try gi.gi_running
try:
    compile('''\
def f():
    yield 1
    yield from g()
    yield 2

def g():
    yield from f()
''', '', 'exec')
except SyntaxError:
    pass
# Try gi.gi_yieldfrom
try:
    [y for x in range(3) for y in gi.gi_yieldfrom]
except SyntaxError:
    pass

def yield_inside():
    yield lambda: None

# Test __qualname__ and __name__
