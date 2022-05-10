import signal
# Test signal.setitimer()
import signal
def call_me(signum,frame):
    print('Inside call_me')
signal.signal(signal.SIGALRM, call_me)
signal.setitimer(signal.ITIMER_REAL, 0.5)
import signal
import time
def on_alarm(signum, stackframe):
    print('Alarm signal handler')
signal.signal(signal.SIGALRM, on_alarm)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
time.sleep(2)
# Test signal.signal()
import signal
def call_me(signum, frame):
    print('Inside call_me')
signal.signal(signal.SIGALRM, call_me)
# Test signal.getsignal()
import signal
def call_me(signum, frame):
    print('Inside call_me')
signal.signal(signal.SIGALRM, call_me)
