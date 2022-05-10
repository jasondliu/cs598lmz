import sys, threading

def run():
  while True:
    sys.stdout.write('p')
    sys.stdout.flush()
    time.sleep(1)

# Start a parallel thread that runs in the background
threading.Thread(target=run).start()

# Run the main thread
while True:
  sys.stdout.write('a\n')
  sys.stdout.flush()
  time.sleep(1)
