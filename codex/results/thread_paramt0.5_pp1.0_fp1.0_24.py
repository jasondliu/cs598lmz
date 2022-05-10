import sys, threading
threading.Thread(target=lambda: sys.stdout.write("This is a thread\n")).start()

# Run a thread that does nothing
threading.Thread(target=lambda: None).start()

# Run a thread that sleeps
threading.Thread(target=lambda: time.sleep(1)).start()

# Run a thread that prints
threading.Thread(target=lambda: sys.stdout.write("This is a thread.\n")).start()

# Run a thread that prints
threading.Thread(target=lambda: sys.stdout.write("This is a thread.\n")).start()

# Run a thread that prints
threading.Thread(target=lambda: sys.stdout.write("This is a thread.\n")).start()

# Run a thread that prints
threading.Thread(target=lambda: sys.stdout.write("This is a thread.\n")).start()

# Run a thread that prints
threading.Thread(target=lambda: sys.stdout.write("This is a thread.\n")).start()

# Run a thread that prints

