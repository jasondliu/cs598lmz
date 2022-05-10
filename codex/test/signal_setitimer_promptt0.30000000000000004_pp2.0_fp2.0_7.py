import signal
# Test signal.setitimer()
#
# This test is a bit tricky because it's hard to test the timer
# without it going off.  We use a very short timer, and we also
# set a signal handler to catch the timer signal.  This handler
# sets a global variable to indicate that the timer went off.
#
# The test is run in a subprocess so that we can set the timer
# and then kill the process.  The parent process waits for the
# child to die, and then checks to see if the timer went off.

# This is set to 1 if the timer goes off.
timer_went_off = 0

# This is set to 1 if the alarm goes off.
alarm_went_off = 0

def handler(signum, frame):
    global timer_went_off
    timer_went_off = 1

def alarm_handler(signum, frame):
    global alarm_went_off
    alarm_went_off = 1

def main():
    global timer_went_off
    global alarm_went_off

