import signal
signal.signal(signal.SIGTERM, signal.SIG_DFL)#to avoid getting killed by group kill
signal.signal(signal.SIGINT, signal.SIG_DFL)#to avoid getting killed by ctrl-c 

error_count = 0
