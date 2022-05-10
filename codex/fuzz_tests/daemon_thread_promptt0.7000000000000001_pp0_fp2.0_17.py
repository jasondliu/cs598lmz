import threading
# Test threading daemon
# Create a new thread object, passing in the function and its arguments.
thread = threading.Thread(target=thread_function, args=(1,))
# Set thread to a daemon thread; which will terminate when the main program terminates.
thread.daemon = True
# Start the thread.
thread.start()
# The main code will execute while the thread executes.
# The main code will wait 1.5 seconds and then terminate, thus killing the thread.


# Test multiprocessing
# Create a new process object, passing in the function and its arguments.
process = multiprocessing.Process(target=process_function, args=(1,))
# Start the process.
process.start()
# The main code will execute while the process executes.
# The main code will wait 1.5 seconds and then terminate, which will not kill the process.
# The process will continue to run until it is finished.
