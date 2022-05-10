fn = lambda: None
# Test fn.__code__.co_firstlineno with submethods

def source_for_test(test):
    source = inspect.getsource(test)
    # note __file__ may be relative
    filename = inspect.getfile(test)
    return filename + ": " + source

def test1():
    def gen():
        def test2():
            print 'test2'
            return gen().__code__.co_firstlineno
        yield test2()
    return gen().next()

def test2():
    def gen():
        def gen2():
            def test3():
                print 'test3'
                return gen2().__code__.co_firstlineno
            yield test3()
        yield gen2().next()
    return gen().next()

def test3():
    def single():
        print 'test4'
        return single().__code__.co_firstlineno
    return single()

print source_for_test(test1)
line1 = test1()
print source_for_test(test2)
line2 = test2()

