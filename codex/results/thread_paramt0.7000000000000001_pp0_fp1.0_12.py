import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from stdout\n')).start()
threading.Thread(target=lambda: sys.stderr.write('Hello from stderr\n')).start()

# Python 2.7
from __future__ import print_function
import sys, threading
threading.Thread(target=lambda: print('Hello from stdout', file=sys.stdout)).start()
threading.Thread(target=lambda: print('Hello from stderr', file=sys.stderr)).start()
</code>

