gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code)
# Test gi.gi_frame
print(gi.gi_frame)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)
# Test gi.send
print(gi.send(1))
# Test gi.throw
try:
    gi.throw(ZeroDivisionError)
except ZeroDivisionError:
    print("ZeroDivisionError")
# Test gi.close
gi.close()

# Test generator
def gen():
    yield 1
    yield 2
    yield 3
    return 4

g = gen()
# Test g.gi_code
print(g.gi_code)
# Test g.gi_frame
print(g.gi_frame)
# Test g.gi_running
print(g.gi_running)
# Test g.gi_yieldfrom
print(g.gi_yieldfrom)
# Test g.send
print(g.send(None))
print(g
