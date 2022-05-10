import select
# Test select.select and select.poll

if hasattr(select, 'poll'):
    @unittest.skipUnless(hasattr(select, 'poll'), 'poll not supported')
    def test_poll(self):
        pollster = select.poll()
        fd = os.open(test.support.TESTFN, os.O_WRONLY | os.O_CREAT)
