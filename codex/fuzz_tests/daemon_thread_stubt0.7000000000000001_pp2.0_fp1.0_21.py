import sys, threading

def run():
  while 1:
    input = raw_input("")
    if input == "quit":
      sys.exit(0)
    else:
      print("error")


thread = threading.Thread(target=run)
thread.start()

while 1:
  pass
