import sys, threading

def run():
  # 用于测试threading.current_threa()方法
  print("Thread name == %s" % threading.current_thread().name)
  sys.exit()

threading.Thread(target=run, name="MyThread").start()
