import sys, threading
threading.Thread(target=lambda:(sys.stdin.readline().strip(), eval(sys.stdin.readline().strip()))).start()
