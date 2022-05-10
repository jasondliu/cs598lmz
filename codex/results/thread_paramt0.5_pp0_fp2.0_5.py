import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, sorted(list(map(int, sys.stdin.read().split()))))))).start()
