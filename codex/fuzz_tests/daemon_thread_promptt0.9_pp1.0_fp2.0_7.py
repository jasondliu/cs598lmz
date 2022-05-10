import threading
# Test threading daemon property
def worker():
    print(threading.current_thread().getName())
    print(threading.current_thread().isDaemon())
    sys.exit(1)

t = threading.Thread(name='non-daemon', target=worker)
print(t.isDaemon())

d = threading.Thread(name='daemon', target=worker, daemon=True)
print(d.isDaemon())

d.start()
t.start()
print(t.is_alive())
print(d.is_alive())
</code>
As John suggested, print the t.is_alive() and d.is_alive() within the worker function.
The output would show that the sysexit() doesn't guarantee thread exit.
As for the "> It seems that i can't pass variables to the thread after changing daemon to True", I also have no idea about it. Your code works fine.


A:

The solution is to add a loop in your main function. While t is working (is_alive is true), check the state of d.
<code
