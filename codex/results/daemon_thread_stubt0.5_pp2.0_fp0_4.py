import sys, threading

def run():
    global thread_count
    
    while thread_count:
        thread_count -= 1
        threading.Thread(target=run).start()

thread_count = int(sys.argv[1])

run()
