gi = (i for i in ())
# Test gi.gi_code
# Test gi.gi_frame
# Test gi.gi_running
# Test gi.gi_yieldfrom
# Test gi.send
# Test gi.throw
# Test gi.close

# Test generators returning objects that support len()
def gen_len():
    yield len
    yield len
    yield len

gl = gen_len()
# Test gl.gi_code
# Test gl.gi_frame
# Test gl.gi_running
# Test gl.gi_yieldfrom

# Test generators returning strings
def gen_str():
    yield str
    yield str
    yield str

gs = gen_str()
# Test gs.gi_code
# Test gs.gi_frame
# Test gs.gi_running
# Test gs.gi_yieldfrom

# Test generators returning strings that support len()
def gen_unicode():
    yield unicode
    yield unicode
    yield unicode

gu = gen_unicode()
# Test gu.gi_code
# Test gu.gi_frame
# Test gu.
