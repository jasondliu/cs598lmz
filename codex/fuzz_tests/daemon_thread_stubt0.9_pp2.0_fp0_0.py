import sys, threading

def run():
    for i in range(0, 10):
        print(sys.argv[1])
        time.sleep(0.5)

n = int(input())

for i in range(0, n):
    t = threading.Thread(target = run, args = [], kwargs = {})
    t.start()
