import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1b]2;NEW_THREAD\x07")).start()

# OR

import threading
threading.Thread(target=lambda: "\x1b]2;NEW_THREAD\x07").start()

# OR

import threading
threading.Thread(target=lambda: print("\x1b]2;NEW_THREAD\x07")).start()
