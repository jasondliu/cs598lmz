import sys, threading

def run():
  while True:
    sys.stdout.write('1')
    sys.stdout.flush()

def main():
  thread = threading.Thread(target=run)
  thread.start()
  while True:
    sys.stdout.write('2')
    sys.stdout.flush()

if __name__ == '__main__':
  main()
