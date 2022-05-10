import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return fd.fileno()
        def close(self):
            a.append(1)

    # Redirect stdout to a pipe, so that if it fails, we'll see the
    # error message on stdout.
    oldout = sys.stdout
    olderr = sys.stderr
    r, w = os.pipe()
    sys.stdout = os.fdopen(w, 'wb')
    sys.stdout.fileno = lambda: w
    sys.stderr = sys.stdout

    try:
        fd = F()
        select.select([fd], [], [])
    except Exception:
        # Uncomment the following line to make the test fail:
        #os._exit(1)
        pass
    sys.stdout.close()
    sys.stdout = oldout
    sys.stderr = olderr
    os.close(r)

    assert a
    assert a[0] == 1

test_select_mutated()
