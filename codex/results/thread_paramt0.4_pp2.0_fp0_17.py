import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(sorted(sys.stdin.read().splitlines())))).start()
