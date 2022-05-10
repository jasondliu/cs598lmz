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

# Test gi.gi_running
try:
    gi.gi_running
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test gi.throw(exception, value)
try:
    gi.throw(Exception, 'test')
except Exception as e:
    print(e)

# Test gi.throw(exception, value, traceback)
try:
    gi.throw(Exception, 'test', None)
except Exception as e:
    print(e)
