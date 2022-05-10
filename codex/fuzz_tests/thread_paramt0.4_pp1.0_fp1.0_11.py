import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()

# Python 3.4
import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input()), daemon=True).start()
</code>

