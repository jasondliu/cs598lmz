import signal
# Test signal.setitimer() works
signal.setitimer(signal.ITIMER_REAL, 1, 0)
signal.pause()

import os

# Test os.fork()
pid = os.fork()
if pid == 0:
    # Child
    print('Hello from child {}'.format(os.getpid()))
    os._exit(0)
else:
    # Parent
    os.waitpid(pid, 0)
    print('Hello from parent {}'.format(os.getpid()))

# Test os.waitpid()
pid = os.fork()
if pid == 0:
    # Child
    print('Hello from child {}'.format(os.getpid()))
    os._exit(0)
else:
    # Parent
    print('Hello from parent {}'.format(os.getpid()))
    os.wait()

# Test os.kill()
pid = os.fork()
if pid == 0:
    # Child
    print('Hello from child {}'.format(os.getpid()))
    os.wait()
else:
    # Parent

