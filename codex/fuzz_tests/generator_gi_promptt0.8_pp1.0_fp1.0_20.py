gi = (i for i in ())
# Test gi.gi_code, gi.gi_frame and gi.gi_running
gi.gi_code
gi.gi_frame
gi.gi_running
# Test gi.gi_yieldfrom
try:
    gi.gi_yieldfrom
except AttributeError:
    pass
else:
    raise RuntimeError('expected AttributeError')
# Test gi.send() and gi.throw()
try:
    gi.send(42)
except StopIteration:
    pass
else:
    raise RuntimeError('expected StopIteration')
try:
    gi.throw(RuntimeError)
except StopIteration:
    pass
else:
    raise RuntimeError('expected StopIteration')

# Test gi.gi_yieldfrom
def yieldfrom_yielder():
    yield from (1, 2, 3)

def yieldfrom_yielder_throw():
    yield from ()
    yield 1
    try:
        yield from yieldfrom_yielder()
    except IndexError:
        yield 42
    yield 3

def yieldfrom_sender(
