import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

s = S(x=1)

def f():
    s.x = 2
    g()

def g():
    pass



"""

def test_not_precise_enough_in_jitdriver_with_exception(monkeypatch):
    def entry_point(args):
        f()
        return 1
    def f():
        l = [1]
        try:
            g(l[1])
        except IndexError:
            pass
    def g(a):
        pass
    else:
        py.test.skip("cpython-only")
    t, typer = get_func_and_typer(f, [int], policy=P_NONE)
    monkeypatch.setattr(typer, '_precise_enough', lambda *args: False)
    typer.annotate_all()
    rtyper = RPythonTyper(typer)
    rtyper.specialize()
    


def test_not_precise_enough_in_jitdriver(monkeypatch):
   
