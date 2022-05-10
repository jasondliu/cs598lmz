import signal
# Test signal.setitimer(), which needs root access
try:
    signal.setitimer(signal.ITIMER_REAL, .01, .01)
except PermissionError:
    raise unittest.SkipTest("Setitimer requires root access, skipping test.")


async def sleep():
    await asyncio.sleep(0.01)


@asyncio.coroutine
def null_coro():
    pass


class TestTimer(unittest.TestCase):

    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(None)

    def tearDown(self):
        # just in case if we have transport close callbacks
        self.loop.stop()
        self.loop.run_forever()
        self.loop.close()

    def test_timer(self):
        timer = self.loop.call_later(0.01, lambda: None)
        timer.cancel()
        self.assertIs(timer.cancelled(), True)
        self.assertIs(timer.cancelled
