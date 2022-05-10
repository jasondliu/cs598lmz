gi = (i for i in ())
# Test gi.gi_code
gi.gi_code
# Test gi.gi_frame
gi.gi_frame
# Test gi.gi_running
gi.gi_running
# Test gi.gi_yieldfrom
gi.gi_yieldfrom

# Test StopIteration
def ff(x):
    yield 1
    raise StopIteration(x)

f = ff(5)
try:
    f.next()
    f.next()
except StopIteration as e:
    print e.args

# Test StopIteration.__init__
def ff(x):
    raise StopIteration(x)

f = ff(())
try:
    f.next()
except StopIteration as e:
    print e.args[0] == ()

# Test GeneratorExit
def ff(x):
    try:
        yield 1
    except GeneratorExit:
        print x
f = ff(5)
f.next()
f.close()

# Test GeneratorExit.__init__
def ff(x):
    try:
        yield 1
    except GeneratorExit
