import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, sorted(map(int, sys.stdin.readlines()))))), daemon=True).start()

# import sys, threading
# threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, sorted(map(int, sys.stdin.readlines()))))), daemon=True).start()

# import sys, threading
# threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, sorted(map(int, sys.stdin.readlines()))))), daemon=True).start()

# import sys, threading
# threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, sorted(map(int, sys.stdin.readlines()))))), daemon=True).start()

# import sys, threading
# threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, sorted(map(int, sys.stdin.
