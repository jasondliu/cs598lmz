import signal
# Test signal.setitimer()
def setitimerTimeout():
    #time.sleep(1)
    print "Received SIGALRM!"
    sys.exit(1)

def callSetitimer():
    signal.signal(signal.SIGALRM, setitimerTimeout)
    signal.setitimer(signal.ITIMER_REAL, 1)
    return "called"

signal.siginterrupt(signal.SIGALRM, True)

#doTests(signalmod,
#        [ ("SIGALRM", "SIGALRM", {"SIGALRM":1}, "SIGCHLD"), #itimer
#          ("zeroDivisionError",
#           "callSetitimer()",
#           None, "ZeroDivisionError"), #itimer
#          ("zeroDivisionError",
#           "callSetitimer()",
#           {"SIGALRM":1}, "Received SIGALRM!"), #itimer
#          ])

# Test signal.set_wakeup_fd()
import os
import socket
if os.name ==
