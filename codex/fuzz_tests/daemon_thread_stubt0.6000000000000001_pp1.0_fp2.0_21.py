import sys, threading

def run():
    while True:
        command = sys.stdin.readline()
        if command == "!exit\n":
            return
        print(command)

t = threading.Thread(target=run)
t.start()

while True:
    sys.stdout.write(">> ")
    command = sys.stdin.readline()
    if command == "!exit\n":
        break
    print(command)

t.join()
