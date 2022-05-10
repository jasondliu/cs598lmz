import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from thread 1\n")).start()
threading.Thread(target=lambda: sys.stdout.write("Hello from thread 2\n")).start()
threading.Thread(target=lambda: sys.stdout.write("Hello from thread 3\n")).start()
threading.Thread(target=lambda: sys.stdout.write("Hello from thread 4\n")).start()
threading.Thread(target=lambda: sys.stdout.write("Hello from thread 5\n")).start()
threading.Thread(target=lambda: sys.stdout.write("Hello from thread 6\n")).start()
threading.Thread(target=lambda: sys.stdout.write("Hello from thread 7\n")).start()
threading.Thread(target=lambda: sys.stdout.write("Hello from thread 8\n")).start()
threading.Thread(target=lambda: sys.stdout.write("Hello from thread 9\n")).start()
threading.Thread(target=lambda: sys.stdout.write("Hello from thread 10\
