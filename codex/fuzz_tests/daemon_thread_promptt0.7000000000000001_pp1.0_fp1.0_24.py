import threading
# Test threading daemon
threading.Thread(target = lambda: time.sleep(3)).start()

# Test threading Event
threading.Event().set()

# Test threading RLock
lock = threading.RLock()
lock.acquire()
lock.release()

# Test threading Condition
condition = threading.Condition()
condition.acquire()
condition.release()
condition.wait()
condition.notify_all()

# Test threading Semaphore
threading.Semaphore().release()

# Test threading BoundedSemaphore
threading.BoundedSemaphore().release()

# Test threading Lock
threading.Lock().release()

# Test threading Timer
threading.Timer(1, lambda: print("Hello")).start()

# Test threading local
threading.local()

# Test threading
threading.active_count()
threading.current_thread()
threading.enumerate()
threading.main_thread()

# Test threading
threading.stack_size([size])

# Test threading Barrier
