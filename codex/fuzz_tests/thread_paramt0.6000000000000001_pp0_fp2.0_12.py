import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(sorted(set([input() for _ in range(int(input()))]))))).start()
