import threading
# Test threading daemon
def f1(nums):
    for num in nums:
        time.sleep(0.2)
        print(num)
    print('Common f1')

def f2(nums):
    for num in nums:
        time.sleep(0.2)
        print(num)
    print('Common f2')

thread1 = threading.Thread(target=f1, args=([10, 20, 30]))
thread2 = threading.Thread(target=f2, args=([100, 200, 300]))

thread1.start()
thread2.start()

thread1.join()
thread2.join() # join the finished thread back to main thread

print('main thread')



# 创建 一个守护线程
d1 = threading.Thread(target=f1, args=([10, 20, 30]))
d1.setDaemon(True) # daemon==True 表示守护线程，
