import sys, threading

def run():
    print("Start")
    time.sleep(2)
    print("End")

if __name__ == "__main__":

    #获取当前线程
    t = threading.current_thread()
    print(t)
    print(t.getName())

    #实例化线程对象
    t1 = threading.Thread(target=run)
    print(t1)

    #启动线程
    t1.start()

    #线程名
    t1.setName("t1")
    print(t1.getName())

    #线程活动状态
    print(t1.is_alive())
