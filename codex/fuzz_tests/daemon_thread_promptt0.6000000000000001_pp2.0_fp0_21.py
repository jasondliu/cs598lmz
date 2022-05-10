import threading
# Test threading daemon
# thread_daemon = threading.Thread(target=loop_daemon)
# thread_daemon.setDaemon(True)
# thread_daemon.start()

# Test threading without daemon
thread_nondaemon = threading.Thread(target=loop_nondaemon)
thread_nondaemon.start()

# Test threading join
# thread_join = threading.Thread(target=loop_join)
# thread_join.start()
# thread_join.join()

# Test threading lock
# thread_lock = threading.Thread(target=loop_lock)
# thread_lock.start()
# thread_lock.join()


# Test threading lock with daemon
# thread_lock_daemon = threading.Thread(target=loop_lock_daemon)
# thread_lock_daemon.setDaemon(True)
# thread_lock_daemon.start()
# thread_lock_daemon.join()

# Test threading lock with daemon
# thread_lock_daemon = threading.Thread(target=loop_lock_
