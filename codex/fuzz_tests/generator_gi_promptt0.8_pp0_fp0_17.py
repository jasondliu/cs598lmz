gi = (i for i in ())
# Test gi.gi_code
# test generator.close()
# return gi
# run_test(test_generator_return)

def test_suspend_generator_after_close():
    """
    def foo():
        i = 0
        while 1:
            yield i
            i += 1
    g = foo()
    g.next()
    g.close()
    try:
        g.next()
    except StopIteration:
        print 'generator closed'
    else:
        print 'generator not closed'
    """

    # test generator close
    foo = """
        def foo():
            i = 0
            while 1:
                yield i
                i += 1
    """

    def test_foo():
        # XXX: can't get this to work yet
        pass
        g = foo()
        g.next()
        g.close()
        try:
            g.next()
        except StopIteration:
            #print 'generator closed'
            pass
        else:
            print 'generator not closed'

    run_test(test_foo
