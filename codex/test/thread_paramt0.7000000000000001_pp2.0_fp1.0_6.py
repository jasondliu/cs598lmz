import sys, threading
threading.Thread(target=lambda: sys.stdout.write('This is\n')).start()
threading.Thread(target=lambda: sys.stdout.write('a thread\n')).start()
threading.Thread(target=lambda: sys.stdout.write('running\n')).start()
 
# The above prints the lines in any order.  This version prints the lines
# in the correct order.

import threading
threading.Thread(target=lambda: sys.stdout.write('This is\n')).start()
threading.Thread(target=lambda: sys.stdout.write('a thread\n')).start()
threading.Thread(target=lambda: sys.stdout.write('running\n')).start()

import threading
threading.Thread(target=lambda: sys.stdout.write('This is\n'), daemon=True).start()
threading.Thread(target=lambda: sys.stdout.write('a thread\n'), daemon=True).start()
