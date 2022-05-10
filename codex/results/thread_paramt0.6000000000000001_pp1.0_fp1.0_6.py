import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello, world\n")).start()

# Python 2.6 and 2.7
import threading
threading.Thread(target=lambda: sys.stdout.write("Hello, world\n")).start()

# Python 3.0
import sys
threading.Thread(target=sys.stdout.write, args=("Hello, world\n",)).start()

# Python 3.1 and above
import sys
threading.Thread(target=sys.stdout.write, args=("Hello, world\n",)).start()

# Python 3.2 and above
import sys
threading.Thread(target=sys.stdout.write, args=("Hello, world\n",)).start()

# Python 3.3 and above
import sys
threading.Thread(target=sys.stdout.write, args=("Hello, world\n",)).start()

# Python 3.4 and above
import sys
threading.Thread(target=sys.stdout.write, args=("Hello, world\n",)).start()

# Python 3
