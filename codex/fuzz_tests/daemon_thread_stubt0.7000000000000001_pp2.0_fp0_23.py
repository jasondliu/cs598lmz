import sys, threading

def run():
    # 请求数据
    data = input('>>: ').strip()
    if data:
        print('你输入的是:', data)
    else:
        print('输入为空')

t = threading.Thread(target=run)
t.start()
t.join()

# 通过多线程来接收键盘数据,阻塞主线程
# t = threading.Thread(target=run)
# t.setDaemon(True)  # 设置为守护线程,必须在start之前设置
# t.start()
# while True:
#     pass
