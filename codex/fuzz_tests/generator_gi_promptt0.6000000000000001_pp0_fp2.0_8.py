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

print(gi.gi_frame.f_code.co_name)

# Test gi.gi_running
try:
    gi.gi_running
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test gi.send
try:
    gi.send(None)
except TypeError:
    print('SKIP')
    raise SystemExit

# Test gi.throw
try:
    gi.throw(StopIteration)
except StopIteration:
    print('StopIteration')

# Test gi.close
try:
    gi.close()
except ValueError:
    print('ValueError')

def gen():
    yield
gen()
