gi = (i for i in ())
# Test gi.gi_code
gi.gi_code
# Test gi.gi_frame
gi.gi_frame
# Test gi.gi_running
gi.gi_running
# Test gi.gi_name
gi.gi_name
# Test gi.gi_filename
gi.gi_filename
# Test gi.gi_lineno
gi.gi_lineno

# Test gi.send()
gi.send(None)
try:
    gi.send('a')
except StopIteration as e:
    # Test gi.throw()
    gi.throw(ValueError)
    try:
        gi.throw(TypeError, 'a')
    except TypeError as e:
        assert str(e) == 'a'

###########################
# Test code.co_filename, co_name, co_firstlineno, co_argcount, co_varnames,
# co_cellvars, co_freevars
###########################
def test_code(a, b=1, *args, **kwargs):
    c = 1
    d = 2
