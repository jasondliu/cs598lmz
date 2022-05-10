import threading
# Test threading daemonic
def f():
  print(threading.currentThread().getName(), 'Starting')
  print(threading.currentThread().getName(), 'Exiting')

def main():
  t = threading.Thread(target=f, name='daemon thread')
  t.setDaemon(True)
  t.start()
  print('done')

if __name__ == '__main__':
  main()
