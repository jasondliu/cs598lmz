import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from thread\n")).start()

# Python 3.4+
import sys, threading
threading.Thread(target=sys.stdout.write, args=("Hello from thread\n",)).start()

# Python 3.5+
import sys, threading
threading.Thread(target=print, args=("Hello from thread",), kwargs=dict(flush=True)).start()
