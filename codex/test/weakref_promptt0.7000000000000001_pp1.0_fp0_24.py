import weakref
# Test weakref.ref(func)
import gc

class C:
    pass

def f(o):
    pass

def g(o):
    pass

def h(o):
    pass

def k(o):
    pass

if __name__ == "__main__":
    import support
    support.run_unittest(TestWeakref)
    support.run_doctest(weakref)

def test_main(verbose=None):
    import doctest

    # Run the doc tests for the builtin weakref module
    import weakref
    globs = weakref.__dict__.copy()
    globs.update(weakref=weakref)
    support.run_doctest(weakref, globs, verbose)

if __name__ == "__main__":
#    test_main(verbose=True)
    test_main()
