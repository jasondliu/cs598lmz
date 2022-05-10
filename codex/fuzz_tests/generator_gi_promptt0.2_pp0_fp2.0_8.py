gi = (i for i in ())
# Test gi.gi_code.co_name
assert gi.gi_code.co_name == '<genexpr>'
# Test gi.gi_frame.f_code.co_name
assert gi.gi_frame.f_code.co_name == '<module>'

# Test gi.gi_frame.f_code.co_name
def f():
    gi = (i for i in ())
    assert gi.gi_frame.f_code.co_name == 'f'
f()

# Test gi.gi_frame.f_code.co_name
def f():
    def g():
        gi = (i for i in ())
        assert gi.gi_frame.f_code.co_name == 'g'
    g()
f()

# Test gi.gi_frame.f_code.co_name
def f():
    def g():
        def h():
            gi = (i for i in ())
            assert gi.gi_frame.f_code.co_name == 'h'
        h()
   
