import sys, threading

def run():
    while True:
        line = sys.stdin.readline()
        if (line):
            print(line)

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

inputkey = ''

while True:
    inputkey = input()
    if inputkey == 'quit':
        break
