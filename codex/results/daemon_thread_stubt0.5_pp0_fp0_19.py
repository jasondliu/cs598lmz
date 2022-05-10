import sys, threading

def run():
    print("Started thread")
    sys.exit()
    print("This line will never be printed")

thread = threading.Thread(target=run)
thread.start()

print("Waiting for thread to finish")
thread.join()
print("Thread finished")
