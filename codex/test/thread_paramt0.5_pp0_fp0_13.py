import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 2\n')).start()

#Output
#Hello from Thread 1
#Hello from Thread 2

#Example 3
#Example 3
import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 2\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 3\n')).start()

#Output
#Hello from Thread 1
#Hello from Thread 2
#Hello from Thread 3

#Example 4
import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 2\n')).start()
