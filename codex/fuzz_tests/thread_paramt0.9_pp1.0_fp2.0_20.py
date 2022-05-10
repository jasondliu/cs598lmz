import sys, threading
threading.Thread(target=lambda: sys.stdout.write('.' * 10000000)).start()
</code>

EDIT: Used <code>sys.stdout.write</code> instead of <code>print</code> so that it won't flush everytime.


