import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(1000000))))).start()
</code>
You can see that the thread is not killed, but the main thread is blocked.

