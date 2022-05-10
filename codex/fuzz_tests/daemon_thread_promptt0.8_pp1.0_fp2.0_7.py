import threading
# Test threading daemon - Will use this later for the threading
# def daemon():
#     p = 0
#     while True:
#         print("daemon", p)
#         p += 1
#         time.sleep(1)

# d = threading.Thread(name='daemon', target=daemon)
# d.setDaemon(True)

# d.start()

# time.sleep(3)

# print("d.isAlive()", d.isAlive())

# def non_daemon():
#     p = 0
#     while True:
#         print("non_daemon", p)
#         p += 1
#         time.sleep(1)

# d = threading.Thread(name='non-daemon', target=non_daemon)

# d.start()

# time.sleep(3)

# print("d.isAlive()", d.isAlive())

# # both daemon and non daemon will run until we kill the program

# # d.join()

# # when we add the join to the
