import sys, threading
threading.Thread(target=lambda: sys.stdout.write(raw_input('Enter: '))).start()
</code>

