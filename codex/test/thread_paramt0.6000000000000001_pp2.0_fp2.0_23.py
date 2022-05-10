import sys, threading
threading.Thread(target=lambda:sys.stdout.write(str(int(input())+int(input())))).start()
