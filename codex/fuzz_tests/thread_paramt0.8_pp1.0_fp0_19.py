import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input()), daemon=True).start()

# Daemon thread will be killed when Python interpreter exits.
# If you want to keep the thread alive, use `join` to wait for the thread to complete.
# A daemon thread will never wait for another thread to complete.
# If a thread isn't daemon, Python interpreter will wait for it to complete before exiting.
