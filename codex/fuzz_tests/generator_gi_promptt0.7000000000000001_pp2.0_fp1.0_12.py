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
try:
    gi.send()
except TypeError:
    print('TypeError')

# Test gi.throw
try:
    gi.throw()
except TypeError:
    print('TypeError')

# Test gi.close
gi.close()

# Test gi.gi_frame.f_back
try:
    print(gi.gi_frame.f_back)
except AttributeError:
    print('AttributeError')

# Test gi.gi_frame.f_builtins
try:
    print(gi.gi_frame.f_builtins)
except AttributeError:
    print('AttributeError')

# Test gi.gi_frame.f_code
try:
    print(gi.gi_
