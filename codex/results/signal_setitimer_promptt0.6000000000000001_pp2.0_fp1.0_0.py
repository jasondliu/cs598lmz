import signal
# Test signal.setitimer()
# import signal
# import time

# def handler(signum, frame):
#     print("Signal handler called with signal", signum)
#     raise OSError("Couldn't open device!")

# signal.signal(signal.SIGALRM, handler)
# signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

# # This open() may hang indefinitely
# fd = os.open('/dev/ttyS0', os.O_RDWR)
# signal.setitimer(signal.ITIMER_REAL, 0)
# print("Got here!")
# os.close(fd)


# import signal
# import time
# import os
# def handler(signum, frame):
#     print("Signal handler called with signal", signum)
#     raise OSError("Couldn't open device!")

# signal.signal(signal.SIGALRM, handler)

# class Timeout():
#     """Timeout class using ALARM signal."""

