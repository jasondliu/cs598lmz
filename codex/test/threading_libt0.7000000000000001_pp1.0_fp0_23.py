import threading
threading.stack_size(67108864)

def thread_job():
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish\n")

def main():
    #创建线程
    added_thread = threading.Thread(target=thread_job,name="T1")
    #开始线程
    added_thread.start()
    print("all done\n")
    
if __name__ == "__main__":
    main()

print("test success\n")
