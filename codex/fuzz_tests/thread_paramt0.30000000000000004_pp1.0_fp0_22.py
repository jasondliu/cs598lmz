import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(100000)))))
</code>
This will print the numbers from 0 to 99999 to the console, but it will do it in the background, so the program will terminate immediately.

