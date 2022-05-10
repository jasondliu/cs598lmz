import signal
signal.signal(signal.SIGINT, signal_handler)
# Start thread
t = threading.Thread(target=thread_main)
t.start()

# Wait for thread to finish
t.join()

print("Exiting Main Thread")
