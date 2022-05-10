import sys, threading

def run():
    parts = sys.stdin.readline().split(' ')
    n = int(parts[0])
    k = int(parts[1])
    b = int(parts[2]) - 1
    cows = []
    for i in range(n):
        cow = int(sys.stdin.readline().strip())
        if i < k:
            cows.append(cow)
        else:
            cows.append(cow)
            cows.pop(0)
            print (cows[b])
run()
#print(threading.main_thread())
#print(threading.enumerate())
