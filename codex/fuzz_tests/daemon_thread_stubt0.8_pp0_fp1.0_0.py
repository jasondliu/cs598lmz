import sys, threading

def run():
  while True:
    print "python"
    sys.stdout.flush()

if __name__ == "__main__":
  thread = threading.Thread(target=run)
  thread.daemon = True
  thread.start()

  run()
