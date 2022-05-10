import signal
# Test signal.setitimer by passing in a very large value and see if it
# returns the correct error code.

# use Python logger, which writes to stderr
log = logging.getLogger("test_big_timer")
log.addHandler(util.SilentHandler())

interval = 60*60*1000
found_error = False

def alarm_handler(a, b):
    global found_error
    found_error = True
    log.error("alarm_handler got called! Should not be called.")

signal.signal(signal.SIGALRM, alarm_handler)
# This should not call the alarm_handler
signal.setitimer(signal.ITIMER_REAL, interval)

# Sleep a bit
time.sleep(2)

if not found_error:
    log.info("Pass")
    sys.exit(0)
else:
    log.error("Fail: SIGALRM was fired.")
    sys.exit(1)
