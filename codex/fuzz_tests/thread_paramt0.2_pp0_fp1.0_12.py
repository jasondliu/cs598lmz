import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(100)))))
</code>

