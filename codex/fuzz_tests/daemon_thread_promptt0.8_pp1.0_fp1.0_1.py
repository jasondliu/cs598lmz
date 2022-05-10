import threading
# Test threading daemon
def thread_test(arg):
    while True:
        print(arg)
        time.sleep(1)
# Initialize threading daemons
thrd1 = threading.Thread(target=thread_test, args=["A"])
thrd1.daemon = True
thrd1.start()

thrd2 = threading.Thread(target=thread_test, args=["B"])
thrd2.daemon = True
thrd2.start()
# Loop for daemon threads
while True:
    pass
 
# Kill Python using "Ctrl-C"
 
# Loop will be interrupted
# and following statement will be executed
print("Done")

#-------------------------------------------------------------------

import threading
# Test threading normal thread
def thread_test(arg):
    while True:
        print(arg)
        time.sleep(1)
# Initialize threading normal threads
thrd1 = threading.Thread(target=thread_test, args=["A"])
thrd1.start()

thrd2 = threading.Thread(target=thread_test
