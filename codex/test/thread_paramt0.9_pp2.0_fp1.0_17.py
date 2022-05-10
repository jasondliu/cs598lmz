import sys, threading
threading.Thread(target=lambda:sys.stdout.write('<p>Too many connections...')).start()
