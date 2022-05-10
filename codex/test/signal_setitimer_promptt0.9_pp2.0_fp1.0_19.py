import signal
# Test signal.setitimer() and signal.getitimer().
itimer = getattr(signal, 'setitimer', None)
getitimer = getattr(signal, 'getitimer', None)
if itimer is not None and getitimer is not None:
    timer = getattr(signal, 'ITIMER_REAL', None)
    if timer is None:
        timer = 1
    itimer(timer, 1, 2)
    assert getitimer(timer) == (1, 2)

# pthread_kill(0, 0) does nothing
import ctypes
if hasattr(ctypes, 'CDLL'):
    libc = ctypes.CDLL('libc.so.6')
    pthread_kill = libc.pthread_kill
    pthread_kill.restype = ctypes.c_int
    pthread_kill.argtypes = [ctypes.c_long, ctypes.c_int]
    pthread_kill(0, 0)

# Check pthread_atfork, pthread_mutex_init, pthread_mutex_lock
