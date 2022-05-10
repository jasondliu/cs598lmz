import sys, threading

def run():
  print("start")
  time.sleep(2)
  print("end")

threading.Thread(target=run).start()

# start
# end

print("main thread")
# main thread
