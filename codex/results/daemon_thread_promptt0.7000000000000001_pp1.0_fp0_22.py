import threading
# Test threading daemon started
threading.Thread(target=lambda: print("This should not be printed")).start()

# Test stdout/stderr redirect
# print("This should not be printed")
# raise Exception("This should not be printed")

# Test stdout/stderr restore
print("This should be printed")
raise Exception("This should be printed")
