import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

if not os.path.exists('/var/run/watchdogd'):
    os.mkdir('/var/run/watchdogd')
state_file = open('/var/run/watchdogd/pid', 'w')
state_file.write(str(os.getpid()))
state_file.close()

log = open('/var/log/watchdogd.log', 'w')

while delays:
    try:
        poll(0.1)
    except:
        log.write(traceback.format_exc())
        log.flush()
        sys.exit(1)

log.close()
