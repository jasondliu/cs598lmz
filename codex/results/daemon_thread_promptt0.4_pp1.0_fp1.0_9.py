import threading
# Test threading daemon

def do_this(what):
    whoami(what)

def whoami(what):
    print("Thread %s says: %s" % (threading.current_thread(), what))

if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        p = threading.Thread(target=do_this, args=("I'm function %s" % n,))
        p.start()

# Threading is a way to run multiple threads in the same program
# A thread is a single execution unit within a program
# Threads can run in parallel as long as they don't share the same resources
# Threads are very useful for I/O bound tasks
# Threads are also useful for CPU bound tasks
# Threads are useful for tasks that are long running
# Threads can be used to run multiple tasks at the same time
# Threads can be used to run multiple tasks in a single program
# Threads are useful for tasks that are long running
# Threads are useful for tasks that are long running
# Threads are useful for
