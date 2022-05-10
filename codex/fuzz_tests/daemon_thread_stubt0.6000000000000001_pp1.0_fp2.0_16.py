import sys, threading

def run():
  while True:
    pass

threads = []

for i in range(100000):
  thread = threading.Thread(target=run)
  thread.start()
  threads.append(thread)

while True:
  pass
