import sys, threading

def run():
  while True:
    cmd = input(">>>").strip()
    if cmd == "quit":
      sys.exit()

    else:
      print("Waiting for command:", cmd)
      time.sleep(10)
      print("Executed:", cmd)

if __name__ == "__main__":
  run()
