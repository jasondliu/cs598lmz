gi = (i for i in ())
# Test gi.gi_code
gi.gi_code

# Test gi.gi_frame
try:
    gi.gi_frame
except RuntimeError as e:
    if str(e) != 'generator already executing':
        raise

# Test gi.gi_running
try:
    gi.gi_running
except RuntimeError as e:
    if str(e) != 'generator already executing':
        raise

# Test gi.gi_yieldfrom
try:
    gi.gi_yieldfrom
except RuntimeError as e:
    if str(e) != 'generator already executing':
        raise

# Test gi.send
try:
    gi.send(None)
except RuntimeError as e:
    if str(e) != 'generator already executing':
        raise

# Test gi.throw
try:
    gi.throw(TypeError)
except RuntimeError as e:
    if str(e) != 'generator already executing':
        raise
