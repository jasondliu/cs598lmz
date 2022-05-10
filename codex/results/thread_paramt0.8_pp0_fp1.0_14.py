import sys, threading
threading.Thread(target=lambda: cool.go(sys.argv)).start()
