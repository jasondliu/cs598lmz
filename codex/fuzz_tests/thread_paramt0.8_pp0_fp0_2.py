import sys, threading
threading.Thread(target=lambda: [sys.stdout.write(str(i) + '\n') for i in range(100)]).start()
print '\n'.join(sys.stdout.readlines())
