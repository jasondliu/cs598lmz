import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()

# print('\n'.join(map(str, [input(), input()])))
