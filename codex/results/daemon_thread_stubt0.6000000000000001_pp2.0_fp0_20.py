import sys, threading

def run():
    while True:
        cmd = input("----> ")
        if cmd == "stop":
            break
        print("Running %s" % cmd)

thread = threading.Thread(target=run)
thread.start()

# Wait to finish
thread.join()

print("Exiting")
