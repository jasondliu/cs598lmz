import sys, threading

def run():
    while True:
        print("hello")
        time.sleep(0.5)

# Create a thread and run the run() function in the thread
thread = threading.Thread(target=run)
thread.start()

print("Press any key to stop the thread")
sys.stdin.read(1)

# Stop the thread
thread.join()
print("Thread stopped")
</code>

