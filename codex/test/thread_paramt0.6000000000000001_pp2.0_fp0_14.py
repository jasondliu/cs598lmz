import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(input() for _ in range(int(input()))))).start()
