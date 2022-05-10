import signal
# Test signal.setitimer()

# This test is only relevant for Unix
if not hasattr(signal, 'setitimer'):
    raise ImportError("No setitimer() in signal module")

# Check that SIGALRM is defined
if not hasattr(signal, 'SIGALRM'):
    raise ImportError("No SIGALRM in signal module")

# Check that SIGALRM is defined
if not hasattr(signal, 'ITIMER_REAL'):
    raise ImportError("No ITIMER_REAL in signal module")

# Check that SIGALRM is defined
if not hasattr(signal, 'ITIMER_VIRTUAL'):
    raise ImportError("No ITIMER_VIRTUAL in signal module")

# Check that SIGALRM is defined
if not hasattr(signal, 'ITIMER_PROF'):
    raise ImportError("No ITIMER_PROF in signal module")

# Check that SIGALRM is defined
