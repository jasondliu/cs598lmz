gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    pass
else:
    print('AttributeError expected')

# Test gi.gi_frame
try:
    gi.gi_frame
except AttributeError:
    pass
else:
    print('AttributeError expected')

# Test gi.gi_running
try:
    gi.gi_running
except AttributeError:
    pass
else:
    print('AttributeError expected')

# Test gi.gi_yieldfrom
try:
    gi.gi_yieldfrom
except AttributeError:
    pass
else:
    print('AttributeError expected')

# Test gi.send()
try:
    gi.send(None)
except StopIteration:
    pass
else:
    print('StopIteration expected')

# Test gi.throw()
try:
    gi.throw(RuntimeError)
except RuntimeError:
    pass
else:
    print('RuntimeError expected')

# Test gi.close()
gi.close()
