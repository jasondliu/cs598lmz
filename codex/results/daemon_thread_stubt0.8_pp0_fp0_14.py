import sys, threading

def run():
    while True:
        userInput = input(">> ")

        if userInput == "exit":
            sys.exit()

        elif userInput.startswith("goto "):
            try:
                pos = int(userInput.split("goto ")[-1])
                mem.ptr = pos
            except:
                pass

        else:
            mem.execute(userInput)

if len(sys.argv) == 2:
    with open(sys.argv[1], "r") as f:
        code = f.read()
    mem = memory(code)
    thr = threading.Thread(target=run).start()
    thr.join()
else:
    print("Usage:")
    print("    python3 main.py <file>")
