import sys, threading
threading.Thread(target=lambda:list(map(sys.stdout.buffer.write, iter(sys.stdin.buffer.read, b'')))).start()

