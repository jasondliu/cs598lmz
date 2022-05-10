import sys, threading

def run():
    global thread_count
    thread_count += 1
    print("thread number: " + str(thread_count))
    sys.exit()

thread_count = 0
while thread_count < 10:
    thread = threading.Thread(target=run)
    thread.start()
