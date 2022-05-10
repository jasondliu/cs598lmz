import sys, threading

def run():
    with open('testfile.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                time.sleep(1)
                continue
            print(line)

t= threading.Thread(target=run)
t.start()

while True:
    num = sys.stdin.readline() 
    with open('testfile.txt', 'a') as f:
        f.write(num)
