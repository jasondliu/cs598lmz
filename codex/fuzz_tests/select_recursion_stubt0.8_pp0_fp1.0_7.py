import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

        def read(self):
            pass
    s = select.select([], [], [F()])
    print(s)

# run_test(name='select_mutated')

def test_reraise_after_return():
    try:
        try:
            pass
        except:
            # We purposely call sys.exc_info() because it keeps a reference to
            # the traceback
            exc_info = sys.exc_info()
            assert exc_info[2] is not None
            return
    finally:
        raise exc_info[0], exc_info[1], exc_info[2]

# run_test(name='reraise_after_return')

print('Tests finished - check the output for errors!')
