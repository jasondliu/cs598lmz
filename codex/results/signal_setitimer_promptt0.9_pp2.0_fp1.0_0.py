import signal
# Test signal.setitimerTypeError: object
signal.setitimerTypeError("alarm", 10)
signal.setitimer("alarm", 10)
