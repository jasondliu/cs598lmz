import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()
print('\n'.join(input() for _ in range(int(input()))))
