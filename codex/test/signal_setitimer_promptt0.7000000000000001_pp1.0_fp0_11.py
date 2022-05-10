import signal
# Test signal.setitimer().  This is a non-portable Linux-only feature, so we
# can't test it on the buildbots.
requires_linux = pytest.mark.skipif(
    "sys.platform != 'linux'", reason="Linux-only functionality")


@requires_linux
def test_itimer():
    def handler(signum, frame):
        pass

    # Let SIGALRM be delivered to our handler.
    signal.signal(signal.SIGALRM, handler)

    # Set the timer for one second.
    signal.setitimer(signal.ITIMER_REAL, 1, 0)

    time.sleep(2)
    # Check the timer was delivered.
    assert signal.getitimer(signal.ITIMER_REAL)[0] == 0


@requires_linux
def test_itimer_0():
    # Make sure the itimer does not fire after we set it to 0
    def handler(signum, frame):
        pass

    signal.signal(signal.SIGALRM, handler)
