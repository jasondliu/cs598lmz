import sys, threading

def run():
    print(threading.currentThread().getName())  # 获取当前线程名字
    for i in range(3):
      time.sleep(1)
      msg = "I'm "+threading.currentThread().name+' @ '+str(i)
      print(msg)
    return

def main():
    for i in range(2):
         t = threading.Thread(target=run)
         # t.setDaemon(True) # 将当前线程设置为守护线程
         t.start()
    t.join()
    print('ending')

if __name__ == '__main__':
  main()
