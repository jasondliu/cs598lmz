gi = (i for i in ())
# Test gi.gi_code.co_name returns "".
(gi.gi_code.co_name for gi in ())

def f():
    g = (x for x in range(0))
    yield
    # Test g.gi_code.co_name returns "foo".
    (g.gi_code.co_name for g in ())
    yield
    g = (y for y in range(0))
    # Test g.gi_code.co_name returns "".
    yield
    (g.gi_code.co_name for g in ())


test_operators()
test_create_codefragment()
test_gens()
test_findclasses()
test_findmodules()

if __name__ == '__main__':
    test_main()
