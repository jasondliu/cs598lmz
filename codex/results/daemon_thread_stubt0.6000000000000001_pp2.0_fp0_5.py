import sys, threading

def run():
    print("start")
    time.sleep(2)
    print("end")

if __name__ == "__main__":
    t = threading.Thread(target=run)
    t.start()
    print("main thread")
    # 关闭线程
    # t.join()
    # 主线程等待子线程执行完毕
