import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()

# Python 3.4+
import threading
threading.Thread(target=input, args=()).start()

# Python 3.4+
import threading, queue
threading.Thread(target=lambda q,x: q.put(x), args=(queue.Queue(), input())).start()

# Python 3.4+
import threading, queue
q = queue.Queue()
threading.Thread(target=q.put, args=(input(),)).start()

# Python 3.4+
import threading, queue
q = queue.Queue()
threading.Thread(target=lambda q,x: q.put(x), args=(q, input())).start()

# Python 3.4+
import threading, queue
q = queue.Queue()
threading.Thread(target=q.put, args=(input(),)).start()

# Python 3.4+
import threading, queue
q = queue.Queue()
threading.Thread(target=lambda q,x: q.put(x), args=(
