import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(1000000)))))
</code>
This will print the numbers 1 to 1,000,000 in order, but it will take a long time.

