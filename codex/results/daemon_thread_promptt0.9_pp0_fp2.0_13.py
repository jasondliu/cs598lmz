import threading
# Test threading daemon mode

# When a thread is created in Python using the threading module its environment includes a reference to the list of threads known by the current process.
# The current process is represented by the _active attribute of the threading module.
# If a thread has this daemonic flag set, it is automatically removed from the list when the thread terminates.
# The Python standard library has a module multiprocessing.dummy which is a wrapper around threading. The pool class in this module supports the daemonic flag and will automatically close upon program shutdown.

# This feature was added since many programs using the pool class do not properly join their threads before exiting.

# Additionally, try using a with statement to make sure that threads don't go rogue.

def print_phrase(phrase):
    print(phrase)

def main():
    t1 = threading.Thread(target=print_phrase, args=('hello world',), daemon=True)
    t1.start()

    t2 = threading.Thread(target=print_phrase, args=('haha',))
    t2.start()

    t1.join()
    t2
