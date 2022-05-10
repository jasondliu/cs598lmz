from types import FunctionType
a = (x for x in [1])
b = (x ** 2 for x in a)
print b.next()

a = (x for x in [1, 2, 3])
try:
    a.send([4, 5])
except TypeError:
    print "Error: type"

try:
    a.send(None)
except TypeError:
    print "Error: type"
except StopIteration:
    print "StopIteration"

try:
    a.next()
except StopIteration:
    print "StopIteration"

def gen():
    yield 'foo'
    yield 1
    yield 10.0
    yield 'bar'

a = gen()
print a.next()
print a.next()
print a.next()
print a.next()

try:
    a.next()
except StopIteration:
    print "StopIteration"

def gen(step):
    while True:
        yield admin.state.schedule.runnable[
            random.randint(0, len(admin.state.schedule.runnable) - 1)].
