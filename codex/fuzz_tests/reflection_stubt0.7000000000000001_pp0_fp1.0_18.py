fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

def run_tests():
    try:
        test_func()
    except TypeError, te:
        assert "code object" in str(te)
        print "TypeError raised as expected"
    else:
        print "Expected TypeError to be raised"

run_tests()
