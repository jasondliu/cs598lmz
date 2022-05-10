import sys, threading

def run():
    print('Hello from child', os.getpid(), threading.current_thread())

t = threading.Thread(target=run)
t.start()
t.join()

print('Hello from parent', os.getpid(), threading.current_thread())
