import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello World\n")).start()
sys.stdout.write("Goodbye World!\n")
</code>

