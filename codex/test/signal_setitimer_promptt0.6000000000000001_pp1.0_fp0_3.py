import signal
# Test signal.setitimer
if hasattr(signal, "setitimer"):
    import time
    import errno

    def handler(signum, frame):
        print("receive signal:", signum)

    signal.signal(signal.SIGALRM, handler)

    t = time.time()
    signal.setitimer(signal.ITIMER_REAL, 2)
    while True:
        try:
            signal.pause()
        except OSError as e:
            if e.args[0] != errno.EINTR:
                raise
            else:
                print("time used:", time.time() - t)
                break
    signal.setitimer(signal.ITIMER_REAL, 0)


# Test signal.set_wakeup_fd
if hasattr(signal, "set_wakeup_fd"):
    import os
    import select
    import errno

    def handler(signum, frame):
        print("receive signal:", signum)

