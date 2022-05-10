import sys, threading

def run():
  cmd = "python pi.py --num-workers 25 --services-grpc"
  os.system(cmd)

thread = threading.Thread(target=run, args=())
thread.start()

print "all started"

# wait for finish
while True:
  a = 1
