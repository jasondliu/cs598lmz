import sys, threading

def run():
    while True:
        try:
            line = sys.stdin.readline()
            if line == '':
                break
            print(line)
        except:
            break

threading.Thread(target=run).start()

while True:
    try:
        line = sys.stdin.readline()
        if line == '':
            break
        print(line)
    except:
        break
