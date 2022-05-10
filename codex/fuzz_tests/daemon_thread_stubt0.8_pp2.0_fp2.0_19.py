import sys, threading

def run():
  os.system('python3 /home/pi/User_Interface/user_interface.py')

def main():
  """The main function. Controls the door lock and marquee."""
  os.system('python3 /home/pi/VMS/marquee.py &')
  time.sleep(0.1)
  os.system('python3 /home/pi/VMS/door_lock.py &')
  time.sleep(0.1)
  threading.Thread(target = run).start()
  while True:
    i = 3
    while i > 0:
      print(i)
      i -= 1
      time.sleep(1)
    if os.path.exists('/home/pi/quit.txt'):
      os.remove('/home/pi/quit.txt')
      os.system('python3 /home/pi/VMS/marquee.py &')
      time.sleep(0.1)
      os.system('python3 /home/pi/VMS/door_lock.py &')
      time.sleep(0
