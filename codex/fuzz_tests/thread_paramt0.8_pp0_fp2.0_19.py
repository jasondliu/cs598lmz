import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(str(i) for i in sorted(int(input()) % 3 - 1 for _ in range(int(input())))) + '\n')).start()
