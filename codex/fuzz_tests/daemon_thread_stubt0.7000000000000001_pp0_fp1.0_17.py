import sys, threading

def run():
    print('Running the program!')
    sys.exit(0)

def daemon():
    print('Starting the daemon!')
    sys.exit(0)

daemon_thread = threading.Thread(name='daemon', target=daemon)
daemon_thread.setDaemon(True)

# main thread
main_thread = threading.current_thread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    print(t.getName())

print(main_thread.getName())
