import sys, threading
threading.Thread(target=lambda: sys.stdout.write("thread1\n")).start()
threading.Thread(target=lambda: sys.stdout.write("thread2\n")).start()
threading.Thread(target=lambda: sys.stdout.write("thread3\n")).start()
threading.Thread(target=lambda: sys.stdout.write("thread4\n")).start()
threading.Thread(target=lambda: sys.stdout.write("thread5\n")).start()
threading.Thread(target=lambda: sys.stdout.write("thread6\n")).start()
threading.Thread(target=lambda: sys.stdout.write("thread7\n")).start()
threading.Thread(target=lambda: sys.stdout.write("thread8\n")).start()
threading.Thread(target=lambda: sys.stdout.write("thread9\n")).start()
threading.Thread(target=lambda: sys.stdout.write("thread10\n")).start()
sys.stdout.write("main\n")
</code
