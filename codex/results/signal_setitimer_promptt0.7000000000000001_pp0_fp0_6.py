import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1)
# Several seconds later
time.sleep(2)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1)
# Several seconds later
time.sleep(2)
# The timer is canceled
signal.setitimer(signal.ITIMER_VIRTUAL, 0)
```

- **ITIMER_PROF**

The timer expires when the process has accumulated both user-mode and kernel-mode CPU time.



## time.sleep()

- **time.sleep(secs)**

Suspend execution for the given number of seconds. The argument may be a floating point number to indicate a more precise sleep time.

The actual suspension time may be less than that requested because any caught signal will terminate the sleep() following execution of that signal's catching routine. Also, the suspension time may be longer than requested by an arbitrary amount because of the scheduling of other activity in the system.

**Note**

If a negative time is given, the function returns immediately. It
