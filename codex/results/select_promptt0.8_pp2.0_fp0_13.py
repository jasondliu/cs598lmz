import select
# Test select.select and select.poll

if hasattr(select, 'poll'):
    @unittest.skipUnless(hasattr(select, 'poll'), 'poll not supported')
    def test_poll(self):
        pollster = select.poll()
        fd = os.open(test.support.TESTFN, os.O_WRONLY | os.O_CREAT)
        try:
            pollster.register(fd, select.POLLOUT)

            # Sanity checks
            self.assertEqual(pollster.poll(), [])
            self.assertRaises(
                select.error, pollster.poll, 0)

            # Make sure the fd is writable
            data = b'x' * support.TEST_BUFFER_SIZE
            # The test file is opened in text mode, so convert the data
            if not isinstance(data, str):
                data = data.decode("ascii")
            data = data.encode(sys.getfilesystemencoding())

            ready = pollster.poll()
            self.assertIn((fd, select
