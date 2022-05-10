import signal
# Test signal.setitimer()

# The following code was used to generate the trace
#
# import os, psutil, time
# import signal
# def handler(signum, frame):
#     print "SIGALRM"
# signal.signal(signal.SIGALRM, handler)
# p = psutil.Process(os.getpid())
# p.nice(1)
# signal.setitimer(signal.ITIMER_REAL, 0.5, 0)
# while True:
#     print "Loop"
#     time.sleep(1)

# ... and then the following to generate the trace
#
# python -m trace --ignore-dir='^(venv)$' --ignore-module='^(__main__|signal|psutil|time|threading|_thread|trace|os)$' --timing --count --trace example.py

# This is the trace generated:
#
# --- modulename: signal, funcname: setitimer
# signal.py(100):         def setitimer(which, seconds, interval=0):
# signal
