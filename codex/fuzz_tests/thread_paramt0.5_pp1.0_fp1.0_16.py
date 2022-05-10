import sys, threading
threading.Thread(target=lambda: sys.stdout.write(raw_input()), args=()).start()
sys.stdout.write(raw_input())
</code>

