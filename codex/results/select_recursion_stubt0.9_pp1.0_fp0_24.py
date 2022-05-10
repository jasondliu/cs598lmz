import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

        def fae(self):
            a.append(0xdead)
            del a[0]
        fer = fae

    select.select([F()], [], [], 0)

def test_mutated_cod():
    class C:
        def x(self):
            C.x.func_code = C.y.func_code
        def y(self):
            pass
    C().x()

def test_mutating_code_rationale(self):
    def f():
        pass
    def g():
        pass
    g.func_code = f.func_code
    pass

def test_mutating_code_rationale2(self):
    a = str("")
    a.__add__ = a.__sub__

def test_weird_cell():
    compilation.transformer_class()
    g = {}
    g["sub_func_code"] = g
    def f():
        g["sub_func_code"] = g
        def g():
            pass
        pass
    f
