import sys, threading
threading.Thread(target=lambda: sys.stdout.write('threading').flush(), daemon=True).start()
print('main')
while 1:
    pass
