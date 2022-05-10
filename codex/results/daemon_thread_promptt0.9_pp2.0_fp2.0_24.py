import threading
# Test threading daemon
def test_threading_Daemon():
    def func(lock):
        with lock:
            print("\nfunc starts...")
        sleep_secs = randint(0.2, 1.0)
        print(f"Now func will sleep for {sleep_secs:.2f} secs.")
        sleep(sleep_secs)
        with lock:
            print("\nfunc ends.\n")
    
    lock = threading.RLock()
    
    # We have to explicitly set the daemon flag to true in the Thread initialization
    t1 = threading.Thread(name="t11", target=func, args=(lock,), daemon=False)
    t2 = threading.Thread(name="t22", target=func, args=(lock,), daemon=True)
    
    t1.start()
    t2.start()
    
    sleep_secs = 1
    print(f"\nMain thread will sleep for {sleep_secs} secs")
    sleep(sleep_secs)
    
    # This is the main thread continuing

