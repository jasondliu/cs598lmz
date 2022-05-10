import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input("What would you like to say?"))).start()
