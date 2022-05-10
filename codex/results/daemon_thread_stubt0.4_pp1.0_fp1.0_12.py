import sys, threading

def run():
    print("hello from new thread")

t = threading.Thread(target=run)
t.start()

# join() blocks the calling thread until the thread whose join() method is called is terminated
t.join()

print("hello from main thread")

# output:
# hello from new thread
# hello from main thread

# if we remove t.join(), we get:
# hello from main thread
# hello from new thread
