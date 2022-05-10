import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()
</code>
(the above code is Python 2 because I don't know a nice way to make Python 3 loop forever on a single line).

