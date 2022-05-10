import sys, threading

def run():
    while True:
        print('Hello')
        time.sleep(1)

t = threading.Thread(target=run)
t.start()

# 等待用户输入，结束程序
sys.stdin.read()
