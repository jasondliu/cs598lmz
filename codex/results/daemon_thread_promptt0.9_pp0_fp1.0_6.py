import threading
# Test threading daemon
def daemon():
    import  time
    print('Start: %s' % time.ctime())
    time.sleep(2)
    print('End: %s' % time.ctime())
if __name__ == '__main__':
    t = threading.Thread(target=daemon)
    t.setDaemon(True)    # 将子线程放在主线程中
    t.start()
    t.join()
    print("All threads have finished....")

    t1 = threading.Thread(target=daemon)
    t1.start()     # 不在主线程中
    t1.join()
    print("All threads have finished....")
