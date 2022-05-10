import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\n".join(map(lambda s: s.replace("T", "U"), sys.stdin.readlines())))).start()
