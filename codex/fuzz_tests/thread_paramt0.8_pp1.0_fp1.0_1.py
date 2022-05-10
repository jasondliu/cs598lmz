import sys, threading
threading.Thread(target=lambda:sys.stdout.write("Hello from thread\n")).start()
 
# Synchronus call
# Since we are not using threading or multiprocessing
# We will also see only after main has finished
def hello_sync():
    print("Hello from sync")
hello_sync()

# Call with threading
def hello_thread():
    print("Hello from thread")
thread = threading.Thread(target=hello_thread)
thread.start()
thread.join() # wait for thread
 
# Call with multiprocessing (fork)
def hello_fork():
    print("Hello from fork")
process = multiprocessing.Process(target=hello_fork)
process.start()
process.join() # wait for process
 
# Call with multiprocessing (pool)
# multicore:
pool = multiprocessing.Pool(processes=4)
# distributed:
pool = multiprocessing.Pool(processes=4,maxtasksperchild=2)
pool.apply(hello_fork) # wait for process
pool.terminate() # shutdown
