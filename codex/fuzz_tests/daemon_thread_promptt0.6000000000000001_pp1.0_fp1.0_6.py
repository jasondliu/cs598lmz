import threading
# Test threading daemon

def thread_main():
    print("Thread started")
    for i in range(0, 10):
        print("Thread:", i)
        time.sleep(0.5)
    print("Thread done")

def main_program():
    print("Main program started")
    t = threading.Thread(target=thread_main)
    #t.daemon = True
    t.start()
    print("Main program done")

main_program()

print("Program done")

# The thread does not get killed when main program exits.
# Try with and without t.daemon.

# When daemon is set, the program exits before thread is finished.
# Otherwise, the program will wait for thread to finish.
# Thread is not interrupted by KeyboardInterrupt.

# When daemon is set, the thread does not get a chance to run.
# The main program exits before the thread can run.

# Without daemon, the thread will run, but main program will wait
# for thread to finish before exiting.

# If you do not want the program to wait, you can call t.join
