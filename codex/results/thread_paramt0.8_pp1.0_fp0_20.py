import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join('Data: %s' % line for line in sys.stdin))).start()
</code>

