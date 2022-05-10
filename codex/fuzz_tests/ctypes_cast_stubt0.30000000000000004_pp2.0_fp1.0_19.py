import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE: https://stackoverflow.com/questions/1112343/how-do-i-capture-sigint-in-python
import signal

class GracefulKiller:
  kill_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)

  def exit_gracefully(self,signum, frame):
    self.kill_now = True

if __name__ == '__main__':
  killer = GracefulKiller()
  while True:
    time.sleep(1)
    print("Doing stuff...")
    if killer.kill_now:
      break
  print("End of the program. I was killed gracefully :)")

# SOURCE: https://stackoverflow.com/questions/1112343/how-do-i-capture-sigint-in-python
import signal

