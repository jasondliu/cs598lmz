import threading
# Test threading daemon and semaphore protection.

semaphore = threading.Semaphore(value=1)

t = threading.Thread(target=counter, args=(semaphore,), daemon=True)
t.start()
t.join(timeout=3)

print(t.is_alive())
