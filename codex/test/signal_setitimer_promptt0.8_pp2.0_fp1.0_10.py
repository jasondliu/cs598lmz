import signal
# Test signal.setitimer
# It is tested in interactive mode only
signal.setitimer(signal.ITIMER_VIRTUAL,0,0)

# FIXME test signal.setprofile, signal.settrace

# Test signal.signal
import signal
signal.signal(signal.SIGALRM, signal.SIG_DFL)
signal.signal(signal.SIGALRM, signal.SIG_IGN)
signal.signal(signal.SIGALRM, signal.default_int_handler)

# Test signal.getsignal
import signal
signal.getsignal(signal.SIGALRM)
signal.getsignal(signal.SIGABRT)

# Test signal.pause
# FIXME signal.pause not supported
#import signal
#signal.pause()

# Test signal.raise_signal
import signal
signal.raise_signal(signal.SIGABRT)

# Test signal.default_int_handler
import signal
