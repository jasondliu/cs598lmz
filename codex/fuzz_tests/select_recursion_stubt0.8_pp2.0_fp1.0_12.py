import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    with pytest.raises(TypeError):
        select.select([F()], [], [], 1)

@pytest.mark.skipif(not hasattr(select, "poll"),
                    reason="select.poll() required for this test")

def test_poll_mutated():
    a = []

    class F:
        def fileno(self):
            test_poll_mutated()
            return a.pop()

    with pytest.raises(TypeError):
        select.poll().register(F())

def test_pathconf():
    assert select.pathconf_names['PC_PIPE_BUF'] == 1

@pytest.mark.skipif(mswindows,
                    reason="Don't have select() semantics on Windows")
def test_example_in_docstring():
    """Select on all files in /dev/fd.

    The expected result is that all character special files and
    directories are readable, all block special files and FIFOs are
    either readable or writable, and all regular files are readable.
