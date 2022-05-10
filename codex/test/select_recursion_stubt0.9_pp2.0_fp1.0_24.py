import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return sys.stdout.fileno()

    F().fileno()
    # bpo-34697: Mutating a list while select() is running is safe
    select.select([], [a], [], seconds=10)


class TestSelectRaisesMainException(unittest.TestCase):

    def test_select_raises_main_exception(self):

        def raises_interrupted_system_call_error():
            raise OSError(errno.EINTR)

        with self.assertRaises(OSError) as cm:
            select.select(
                rlist=raises_interrupted_system_call_error(),
                wlist=raises_interrupted_system_call_error(),
                xlist=raises_interrupted_system_call_error())

        self.assertEqual(cm.exception.errno, errno.EINTR)

