import sys, threading

def run():
    print('Thread started')
    time.sleep(1)
    print('Thread ended')
    
def main():
    print('Main started')
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print('Main ended')
    
if __name__ == "__main__":
    main()

# join() method waits until the thread terminates.

# Main started
# Thread started
# Thread ended
# Main ended


# If the main thread exits while other threads are still running, the
# program will exit without waiting for those threads to finish.

# If the main thread exits while other threads are still running, the
# program will exit without waiting for those threads to finish.
# This is usually not what we want.
# To prevent this, we can use the join() method.

# join() method waits until the thread terminates.

# Main started
# Thread started
# Thread ended
# Main ended
