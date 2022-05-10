fn = lambda: None
gi = (i for i in ())
fn.__code__ = mock.sentinel.code
gi.gi_code = fn.__code__
gi.gi_frame = mock.sentinel.frame
gi.gi_running = True
sys.getobjects = (gi,)


class TestPdbOverrides(TestCase):

    def test_usage_of_sys_last_traceback(self):
        class DummyFunction():
            """Used to check sys.last_traceback is used"""
            def __call__(self, *args, **kwargs):
                """Check sys.last_traceback is used"""
                assert sys.last_traceback is not None
                DummyFunction.call_count += 1
        DummyFunction.call_count = 0
        old = sys.last_traceback
        sys.last_traceback = DummyFunction()
        pdb.Pdb()._cmdloop()
        sys.last_traceback = old
        assert DummyFunction.call_count == 1

    def test_post_mortem(self):
        with mock.patch('pdb.Pdb._cmdloop') as cmd_loop:
           
