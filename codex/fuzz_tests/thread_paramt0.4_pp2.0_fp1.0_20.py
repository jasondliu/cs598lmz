import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(100000)))))
</code>
This will write the numbers from 0 to 99999 to stdout, one per line, but it will do so in the background, so your program can continue to run.

