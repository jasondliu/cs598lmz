import threading
# Test threading daemon
import time

def func():
  while True:
    print(threading.current_thread().getName())
    time.sleep(1)

t = threading.Thread(target=func)
t.setDaemon(True)
t.start()

t.join(3)
print("Main thread")

# Test threading lock
import time
import threading

class Account(object):
  def __init__(self):
    self._balance = 0
    self._lock = threading.Lock()

  def deposit(self, money):
    self._lock.acquire()
    try:
      new_balance = self._balance + money
      time.sleep(0.01)
      self._balance = new_balance
    finally:
      self._lock.release()

  @property
  def balance(self):
    return self._balance

class AddMoneyThread(threading.Thread):
  def __init__(self, account, money):
    super().__init__()
    self._account = account
    self._money = money

  def run
