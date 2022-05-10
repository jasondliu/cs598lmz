import threading
# Test threading daemon:
# -program will continue to run in the event of an error
# -python threads are terminated once the program reaches it's end
def throw_error():
	a = 1/0
	return

threading.stack_size(128 * 1024 * 1024) # Change thread stack size to max 128 MB
thread = threading.Thread(target=throw_error, args=()) # Target gets args as a tuple
thread.daemon = True # When True program will continue to run even if there is an error
thread.start()


print "thread history on",  threading.current_thread()
print threading.enumerate()
print thread.is_alive(), "thread daemon", thread.daemon
print threading.active_count()
print "Main thread identifier", threading.main_thread()
print "thread name identity", threading.name_thread()
print threading.ident, "thread identity"

# Test threading locks (RLock is re-entrant lock)
thread_lock = threading.Lock()
thread_rlock = threading.RLock()
try:
	thread_lock
