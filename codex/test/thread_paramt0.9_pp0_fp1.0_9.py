import sys, threading
threading.Thread(target=lambda: sys.stdin.read()).start()

#

import threading
t = threading.Thread(target=some_function_i_want_to_run)
t.setDaemon(True)
t.start()

#

foo = lambda x: x+1
