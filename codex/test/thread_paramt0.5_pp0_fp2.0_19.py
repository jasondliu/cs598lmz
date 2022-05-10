import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input()), daemon=True).start()
print('pong')
