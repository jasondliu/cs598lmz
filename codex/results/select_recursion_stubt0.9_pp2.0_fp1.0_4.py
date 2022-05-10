import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return True

    a.append(F());

    try:
        select.select(a, a, a);
        assert False
    except IndexError:
        pass
    except:
        assert False

    assert a == []    # trigger delayed deletion => segfault

def test_func_module():
    from sys import modules

    # get a func with a module
    f = map

    name = f.__module__
    oldname = modules[name].__name__
    modules[name].__name__ = 'zzz'

    assert repr(f).find('map') >= 0
    assert repr(f).find('zzz') == -1
    assert repr(f).find(name) >= 0

    modules[name].__name__ = oldname
