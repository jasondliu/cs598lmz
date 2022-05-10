from types import FunctionType
list(FunctionType(lambda: None))

class TestSimpleIter(object):
    def test_simple_iter(self):
        for itype in (str, unicode, list, tuple):
            s = itype('abc')
            it1 = iter(s)
            it2 = iter(s)
            assert it1.next() == 'a'
            assert it1.next() == 'b'
            assert it2.next() == 'a'
            assert it1.next() == 'c'
            raises(StopIteration, it1.next)
            raises(StopIteration, it2.next)
    
            # empty iterable
            # XXX: currently, it crashes at rpython level.
            continue
            s = itype('')
            it = iter(s)
            raises(StopIteration, it.next)

    def test_simple_iter_iter(self):
        def f():
            yield 12
            yield 34
        i = iter(iter(f()))
        assert i.next() == 12
        assert i.next() == 34
        raises(Stop
