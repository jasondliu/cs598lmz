import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(100000))))).start()

# To print the numbers from 1 to 100000 without using any loop or recursion
import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(1, 100001))))).start()

# To print the numbers from 1 to 100000 without using any loop, recursion or the range function
import sys, threading
