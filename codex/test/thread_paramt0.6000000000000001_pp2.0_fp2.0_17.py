import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\n".join(map(str, (x[1] for x in sorted(list(map(int, sys.stdin.readlines())), key=lambda x: x[1])))) + "\n")).start()
