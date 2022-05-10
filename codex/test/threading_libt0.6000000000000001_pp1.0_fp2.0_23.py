import threading
threading.Thread(target=test).start()

# 不加这一句，程序不会结束
raw_input()
