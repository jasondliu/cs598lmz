gi = (i for i in ())
# Test gi.gi_code.co_name
assert_equal(gi.gi_code.co_name, "gi")
# Test gi.gi_frame.f_code.co_name
assert_equal(gi.gi_frame.f_code.co_name, "generator_exception_test")

# Test gi.gi_frame.f_lasti
def generator_exception_f_lasti_test():
    i = 0
    g = (i for i in range(10))
    try:
        next(g)
    except Exception:
        pass
    assert_equal(g.gi_frame.f_lasti, 0)
generator_exception_f_lasti_test()

# Test gen.gi_frame.f_lasti
def generator_f_lasti_test():
    def f():
        i = 0
        while True:
            i = yield i
            if i == None:
                break

    g = f()
    assert_equal(g.gi_frame.f_lasti, -1)

    g.send(None)
