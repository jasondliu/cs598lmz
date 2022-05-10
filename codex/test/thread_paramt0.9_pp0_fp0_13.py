import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Coucou\n")).start()
