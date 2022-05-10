import signal
# Test signal.setitimer()
#
# The signal.ITIMER_REAL timer is decremented in real-time, and delivers
# SIGALRM upon expiration.
#
# The signal.ITIMER_VIRTUAL timer is decremented only when the process is
# executing, and delivers SIGVTALRM upon expiration.
#
# The signal.ITIMER_PROF timer is decremented both when the process is
# executing and when the system is executing on behalf of the process. Coupled
# with ITIMER_VIRTUAL, this timer is usually used to profile the time spent by
# the application in user and kernel space. SIGPROF is delivered upon expiration
#
# On the other hand, the remaining interval is still returned from
# signal.getitimer() (the documentation is not very clear about that point;
# see issue #11574).
#
# The setitimer() function sets the specified timer to a value that expires in
# sec seconds and usec microseconds.
# If the it_value member of the value argument is non-zero, the timer is started.
# If the it_interval member of the value argument is
