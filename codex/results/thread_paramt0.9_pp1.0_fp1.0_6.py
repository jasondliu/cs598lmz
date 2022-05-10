import sys, threading
threading.Thread(target=lambda: sys.stdout.write('spam\n')).start()
threading.Thread(target=lambda: sys.stdout.write('SPAM\n')).start()
print('eggs')

"""
As this is supposed to be a multithreaded script, the output must be within any of the two following possibilities:

SPAM
spam
eggs
or

spam
SPAM
eggs

Neither of these is true, as the output of this code is always this:

eggs
spam
SPAM
"""
