import sys, threading
threading.Thread(target=lambda: sys.stdout.write('spam\n')).start()

timers = threading.Timer(5, lambda: sys.stdout.write('5s\n'))
timers.start()
con = lambda: sys.stdout.write('ctrl+c\n')
timers.cancel()

threading.Thread(target=con).start()
