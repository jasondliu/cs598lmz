import sys, threading
threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()

# python3 -c 'import sys, threading; threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()'
