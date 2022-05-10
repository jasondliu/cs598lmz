import threading
# Test threading daemon mode

# Threading daemon mode
# The daemon mode will stop the thread once the main process is done

def func():
    print("Start")
    time.sleep(5)
    print("End")
    
t = threading.Thread(target=func)
t.setDaemon(True)
t.start()
print("Main Thread")

# Output:
# Main Thread
# Start
# End

# Test threading daemon mode with join

# Threading daemon mode
# The daemon mode will stop the thread once the main process is done

def func():
    print("Start")
    time.sleep(5)
    print("End")
    
t = threading.Thread(target=func)
t.setDaemon(True)
t.start()
print("Main Thread")
t.join()
print("Main Thread End")

# Output:
# Main Thread
# Start
# End
# Main Thread End

# Test threading daemon mode with join

# Threading daemon mode
# The daemon mode will stop the thread once the main process is done

def func
