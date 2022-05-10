import sys, threading

def run():
    sys.stdout.write("hey\n")

threads = [ threading.Thread(target=run) for i in range(10) ]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
