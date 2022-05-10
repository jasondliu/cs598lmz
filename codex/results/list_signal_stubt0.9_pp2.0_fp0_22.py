import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        return

    # All done
    signal.setitimer(signal.ITIMER_REAL, 0)
    print("All timers fullfilled")
    sys.exit(0)

# Schedule the first 'alarm' (time for the first one to fire is chosen
# randomly in the loop above)
handler()

# Enter the main loop of the program, displaying the time of day
# until the "alarm" fires
try:
    while True:
        localtime = time.localtime(time.time())
        result = time.asctime(localtime)
        print("The time is: {}".format(result))
        time.sleep(1e-1)
except KeyboardInterrupt:
    pass
