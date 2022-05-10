import signal
# Test signal.setitimer

from test.support import run_unittest, reap_children, get_attribute

import _testcapi

timeout = 10.0

# Create a signal handler.
def handler(signum, frame):
    print("SIGALRM")
    # Force another signal.
    signal.alarm(timeout)

def handler2(signum, frame):
    print("SIGALRM2")

def alarm_interval_and_itimer(interval, itimer):
    signal.signal(signal.SIGALRM, handler)
    # Create itimer on behalf of worker subprocess.
    signal.setitimer(itimer, interval, interval)
    # Create worker and wait for it to exit.
    pid = os.fork()
    if pid == 0:
        # Worker.
        time.sleep(timeout * 2.0)
        os._exit(0)
    pid2, exit_code = os.waitpid(pid, 0)
    # Reap zombie.
    assert pid2 == pid
    assert exit_code == 0

class
