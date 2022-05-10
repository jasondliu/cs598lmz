import threading
# Test threading daemon
def test_daemon():
    print('Start')
    time.sleep(2)
    print('End')

if __name__ == '__main__':
    print('Main begin')
    t = threading.Thread(target=test_daemon)
    t.setDaemon(True)
    t.start()
    print('Main end')
# Main begin
# Start
# Main end
# End

# 使用锁Lock
import time
import threading

class Account:

    def __init__(self):
        self.__balance = 0
        self.lock = threading.Lock()

    def deposit(self, money):
        # 先获取锁才能执行后续的代码
        self.lock.acquire()
        try:
            # 计算存款后的余额
            new_balance = self.__balance + money
            # 模拟受理存款
