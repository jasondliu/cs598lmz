import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(100)))))

# 方法二
# import threading
# def thread_main(loop,nsec):
#     print("thread %s will sleep %s seconds." %(loop,nsec))
#     time.sleep(nsec)
#     print("thread %s ended." %loop)
#
# threads = []
# for i in range(1,6):
#     t = threading.Thread(target=thread_main,args=(i,i))
#     threads.append(t)
#
# if __name__ == "__main__":
#     for t in threads:
#         t.start()
#     print("main thread ended.")
