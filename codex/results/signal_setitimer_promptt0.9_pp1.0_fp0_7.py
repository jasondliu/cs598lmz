import signal
# Test signal.setitimer in Python code
def sighandler(signum, frame):
  print "Signal", signum, "recieved. Frame instance:", frame

signal.signal(signal.SIGVTALRM, sighandler)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.2)
import time
time.sleep(5)
signal.setitimer(signal.ITIMER_VIRTUAL, 0, 0)
# Test signal.setitimer in C module
Process.execl("/proc/self/exe", "/proc/self/exe", os.path.join(os.path.dirname(__file__), "c_itimer.so"), str(getpid()), "0.1", "0.2");
time.sleep(5)
Process.execl("/proc/self/exe", "/proc/self/exe", os.path.join(os.path.dirname(__file__), "c_itimer.so"), str(getpid()), "0", "0");
passed("self-
