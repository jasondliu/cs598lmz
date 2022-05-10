import sys, threading

def run():
    for x in range(0, 100):
        sys.stdout.write("\r%d%%" % x)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\rDone!\n")

print("Starting...")
threading.Thread(target=run).start()
print("While that's running, do something else!")

input("\nPress enter to continue...")
