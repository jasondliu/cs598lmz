import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(None)
    f = F()
    funcname = f.fileno.__code__.co_name
    jitdriver = JitDriver(greens = ['funcname'], reds = [])
    def f1():
        jitdriver.jit_merge_point(funcname=funcname)
        select.select([f], [], [], 0)
    for i in range(20):
        f1()
        assert not a
