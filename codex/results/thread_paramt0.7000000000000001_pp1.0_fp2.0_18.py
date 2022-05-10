import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, sorted(map(int, sys.stdin.readlines()))))))\
.start()
