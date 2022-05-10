import sys, threading

def run():
    print("Hello from " + threading.current_thread().name)
    return

thread = threading.Thread(target=run)
thread.name = "Worker 1"
thread.start()
thread.join()

print("Hello from " + threading.current_thread().name)
print("Done")
