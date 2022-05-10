import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    def test():
        select.select([F()], [], a)

    test()
    test()

def test_select_large():
    reader, writer = os.pipe()
    writer = os.fdopen(writer, 'w')
    data = 'x' * (1 << 23)
    try:
        with open('/dev/null') as f:
            select.select([reader], [], [], 1)    # crash
            writer.write(data)
            writer.close()
            assert f.read(1) == 'x'
    finally:
        os.close(reader)

def test_flushing():
    # See issue #15343
    import codecs
    # CPython does not flush the buffer when exiting the context manager
    try:
        with codecs.open(os.devnull, "w", "utf-8") as f:
            pass
    except UnicodeError:
        py.test.xfail("unicode error")
    # CPython flushes the buffer when exiting the context manager
