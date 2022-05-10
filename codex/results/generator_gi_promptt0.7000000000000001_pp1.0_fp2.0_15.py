gi = (i for i in ())
# Test gi.gi_code, .gi_frame and .gi_running
print(gi.gi_code)
print(gi.gi_frame)
print(gi.gi_running)

# Test gi.send(value)
print('send(None)  -->', gi.send(None))
print('send(42)    -->', gi.send(42))
print('send(raise) -->', end=' ')
try:
    gi.send(raise_exc)
except Exception as exc:
    print(exc)

# Test gi.throw(type[, value[, traceback]])
print('throw(IndexError)         -->', end=' ')
try:
    gi.throw(IndexError)
except IndexError:
    print('IndexError')
print('throw(IndexError, 42, 0) -->', end=' ')
try:
    gi.throw(IndexError, 42, 0)
except IndexError as exc:
    print('%s (%d)' % (exc, exc.args[0]))

# Test gi.close()
print('close
