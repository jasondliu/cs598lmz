import threading
# Test threading daemon
def printit():
  threading.Timer(5.0, printit).start()
  print("Hello, World!")

# printit()

# Test multi threading

# def worker(num):
#     """thread worker function"""
#     print(num)
#     time.sleep(num)
#     return

# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker, args=(i,))
#     threads.append(t)
#     t.start()
