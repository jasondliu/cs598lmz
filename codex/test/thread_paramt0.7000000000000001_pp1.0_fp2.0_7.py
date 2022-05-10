import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'*int(input()))).start()
