import sys, threading

def run():
  global lx
  lx = LedController()
  lx.setup()
  while True:
    lx.loop()

def sleeptest():
  while True:
    time.sleep(1)

def job():
  #threading.Timer(10.0, job).start()
  threading.Thread(target = sleeptest).start()
  print "Sleeping for 5 seconds..."
  time.sleep(5)
  print "done!"

def main():
  #threading.Timer(10.0, job).start()
  threading.Thread(target = run).start()
  #threading.Thread(target = sleeptest).start()
  job()


if __name__ == '__main__':
  main()
