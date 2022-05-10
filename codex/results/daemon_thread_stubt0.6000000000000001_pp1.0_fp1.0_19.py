import sys, threading

def run():
    while True:
        print('Hello from thread {}'.format(threading.current_thread()))
        time.sleep(3)

t = threading.Thread(target=run)
t.daemon = True
t.start()

# while True:
#     print('Hello from thread {}'.format(threading.current_thread()))
#     time.sleep(3)

print('Hello from thread {}'.format(threading.current_thread()))
