import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(10**5))))).start()
</code>
This will print the numbers from 0 to 999999, but it will take a long time.

