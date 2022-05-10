import threading
threading.Thread(target=f).start()

print( 'We are in the main thread')

# We are in the main thread
# Hello from another thread
# Bye from another thread
