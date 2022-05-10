import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(''.join(str(p) for p in range(1, m + 1)) for m in range(1, int(input()) + 1)))).start()
