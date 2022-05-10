import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()

# Python 3.6+
import sys, threading
threading.Thread(target=sys.stdout.write, args=(input(),)).start()

# Python 3.6+
import sys, threading
