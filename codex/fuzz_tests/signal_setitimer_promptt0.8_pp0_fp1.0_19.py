import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 2, 0)
# Test signal.SIGALRM
signal.signal(signal.SIGALRM, lambda *args: 0)

# sys
import sys
# Test sys.maxsize
sys.maxsize > 0
# Test sys.stdin/stdout/stderr
sys.stdin.read(0)
sys.stdout.write('')
sys.stderr.write('')
# Test sys.exit()
sys.exit(0)

# thread
import thread
# Test thread.start_new_thread()
def f(): pass
thread.start_new_thread(f, ())
# Test thread.exit_thread()
thread.exit_thread()
# Test thread.allocate_lock()
l = thread.allocate_lock()
assert l.acquire()
l.release()

# time
import time
# Test time.time()
t = time.time()
# Test time.sleep()
time.sleep(1.0)

#
