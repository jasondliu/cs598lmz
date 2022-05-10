import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    f = F()
    sel = select.select([f], [], [])
</code>
This takes ~3ms on my machine, which confirms the guess that this is not a critical path. I'd still double check the function with a profiler to be sure, but it sounds safe to replace <code>select()</code> with <code>epoll()</code>.

