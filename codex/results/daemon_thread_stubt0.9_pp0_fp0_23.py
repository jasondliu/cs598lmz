import sys, threading

def run():
  print "Thread starts"
  if sys.argv[1] == "recv":
    p = Popen(["python", "test_listen.py"])
  else:
    p = Popen(["python", "test_connect.py"])

  try:
    p.wait()
    print "Wait done, result: %d" % p.returncode
  except KeyboardInterrupt:
    print "KeyboardInterrupt, terminating child"
    p.terminate()

if __name__ == "__main__":
  run()
