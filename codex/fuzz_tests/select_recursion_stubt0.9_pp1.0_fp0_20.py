import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return id(a)

    f = F()
    select.select([f], [], [])        # works fine
    select.select([f], [f], [])       # modifies argument list in-place

def test_xrange_unpack_select():
    for _ in xrange(1, 10):
        test_select_mutated()

try:
    test_xrange_unpack_select()
except ZeroDivisionError:
    print("SKIP")
    import sys
    sys.exit()
