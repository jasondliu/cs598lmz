import sys, threading
threading.Thread(target=lambda: sys.stdout.write("thread_1\n")).start()
threading.Thread(target=lambda: sys.stdout.write("thread_2\n")).start()

sys.stdout.flush()
sys.stdout.flush()
sys.stdout.flush()
sys.stdout.flush()
