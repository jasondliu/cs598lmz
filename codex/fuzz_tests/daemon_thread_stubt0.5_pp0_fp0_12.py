import sys, threading

def run():
    while True:
        cmd = input(">>> ")
        if cmd == "stop":
            break
        print(cmd)

t = threading.Thread(target=run)
t.start()

# sys.exit()

while True:
    print("running")
    time.sleep(1)
