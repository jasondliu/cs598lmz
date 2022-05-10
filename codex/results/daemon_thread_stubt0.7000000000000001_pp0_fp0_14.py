import sys, threading

def run():
  print "running"

def main():
  for i in range(5):
    t = threading.Thread(target=run)
    t.start()

if __name__ == "__main__":
  main()
