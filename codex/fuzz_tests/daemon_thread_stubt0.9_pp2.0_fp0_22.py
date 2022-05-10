import sys, threading

def run():
  print("RUNNING")

print("BEFORE THREAD")
threading.Thread(target=run).start()
print("AFTER THREAD")
