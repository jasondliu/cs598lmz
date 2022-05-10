import sys, threading
threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()
sys.stdout.write("[*] Echo server running")
