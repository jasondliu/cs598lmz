import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    F = F()

    def do(func):
        rv = func(a, [], [F])
        print('>>>', func.__name__, rv)
        a.append(1)

    do(select.select)
    print("[Should have crashed by now]")

Makefile("""
all clean:
""")

try:
    test_select_mutated()
except:
    pass
