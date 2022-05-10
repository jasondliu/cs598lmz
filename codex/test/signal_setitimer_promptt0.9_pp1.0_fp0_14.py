import signal
# Test signal.setitimer() using alarm().

signal.SIGALRM = signal.SIGUSR1
# Upstream signal.SIGALRM is not defined on Android

def setitimer_alarm_cb(signum, frame):
    print("setitimer_alarm_cb")

# Install signal handler
signal.signal(signal.SIGALRM, setitimer_alarm_cb)

signal.setitimer(signal.ITIMER_REAL, 2, 0)

bsp_led_init()
bsp_led_set(1)

time.sleep(3)

signal.setitimer(signal.ITIMER_REAL)
bsp_led_set(0)

