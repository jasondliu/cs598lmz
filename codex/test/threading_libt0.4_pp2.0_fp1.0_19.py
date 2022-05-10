import threading
threading.Thread(target=run).start()

# 每隔5秒检测一次队列是否有待完成的任务，如果有就把第一个任务取出来执行
while True:
    time.sleep(5)
    if not workQueue.empty():
        url = workQueue.get()
        print(url)
        downLoad(url)
        print(url + '下载完成')
        print('*' * 50)
