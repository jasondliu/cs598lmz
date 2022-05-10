import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from\nThread {}\n'.format(threading.current_thread()))).start()

# Hello from
# Thread <_MainThread(MainThread, started 140735016906176)>

# Threading is a way to run multiple threads of execution concurrently. A thread is a single sequence of instructions within in a process. 
# A process is an instance of a running program.
# The example above starts a new thread with the target function lambda: sys.stdout.write('Hello from\nThread {}\n'.format(threading.current_thread()).
# The lambda function is executed concurrently with the main program. The threading.current_thread function returns the thread on which the function is running.
# The threading.Thread class represents an activity that is run in a separate thread of control. 
# There are a number of ways to start a thread in Python. In the example above, the target function is passed to the constructor of the Thread class.
# The thread is started by calling the start method, which calls the run method.

# The run method just calls the target function passed to
