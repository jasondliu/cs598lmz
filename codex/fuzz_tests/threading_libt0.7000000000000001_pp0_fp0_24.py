import threading
threading.stack_size(67108864) # 64MB stack

def do_job(tid):
  # print 'hello from thread',tid
  pass

def main():
  for i in range(0, 1000000):
    thread = threading.Thread(target=do_job, args=(i, ))
    thread.start()

if __name__ == "__main__":
  main()
