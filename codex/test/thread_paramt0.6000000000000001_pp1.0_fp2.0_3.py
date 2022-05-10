import sys, threading
threading.Thread(target=lambda: sys.stdout.write(''.join(sys.stdin.readlines()))).start()
