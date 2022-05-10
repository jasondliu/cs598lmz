gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test gi.gi_frame
try:
    gi.gi_frame
except AttributeError:
    print('SKIP')
    raise SystemExit

def f():
    yield 1

g = f()
print(g.gi_code)
print(g.gi_frame)

# Test gi.gi_running
try:
    gi.gi_running
except AttributeError:
    print('SKIP')
    raise SystemExit

print(gi.gi_running)
print(g.gi_running)

# Test gi.gi_yieldfrom
try:
    gi.gi_yieldfrom
except AttributeError:
    print('SKIP')
    raise SystemExit

print(gi.gi_yieldfrom)
print(g.gi_yieldfrom)
