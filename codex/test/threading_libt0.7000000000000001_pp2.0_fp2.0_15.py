import threading
threading.Thread(target=run_thread,args=(5,)).start()

#Python中使用了GIL来确保同一时刻只有一个线程在一个CPU上执行字节码，无法将多个线程用于多核任务
#如果一个线程执行io操作，那么就会释放GIL，让其他线程有机会执行
#要实现多核任务，最简单的方法是多进程，其他方法是C扩展
#多线程程序偶尔会出
