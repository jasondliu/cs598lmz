import sys, threading
threading.Thread(target=lambda: (sys.stdin.readline(), print(input() + ' ' + input() + ' ' + input()))).start()
