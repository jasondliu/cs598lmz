import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from the other thread!\n")).start()

# Python 3.5+
import sys, threading
threading.Thread(target=sys.stdout.write, args=("Hello from the other thread!\n",)).start()
</code>

