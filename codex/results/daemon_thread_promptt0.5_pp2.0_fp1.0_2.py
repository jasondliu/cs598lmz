import threading
# Test threading daemon

# Create a threading object

threading.Thread(target=print, args=("Hello World!",)).start()

# Create a threading object, and set the daemon

threading.Thread(target=print, args=("Hello World!",), daemon=True).start()

# Create a threading object, and set the daemon
# This will cause the thread to stop when the main thread stops

threading.Thread(target=print, args=("Hello World!",), daemon=True).start()

# Create a threading object, and set the daemon
# This will cause the thread to stop when the main thread stops

threading.Thread(target=print, args=("Hello World!",), daemon=False).start()

# Create a threading object, and set the daemon
# This will cause the thread to stop when the main thread stops
# By default, the daemon is set to False

threading.Thread(target=print, args=("Hello World!",)).start()

# Create a threading object, and set the daemon
# This will cause the thread to stop when the main thread stops
# By default
