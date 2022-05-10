import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x07')).start()
import time
time.sleep(1)
print('時間になりました')

# タイマーをセットする関数
def set_timer(num, callback):
  timer = threading.Timer(num, callback)
  timer.start()

# 3秒後に発火するタイマー
def hello():
  print('hello')
set_timer(3, hello)

# スレッドを使うこともできる
import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x07')).start()

# スレッドを停止させる
import threading

# 停止させるスレッド
def print_numbers():
  for i in range(1, 1000000000):
    print(i)

thread = threading.Thread(target=print_numbers)
thread.start()

#
