import threading
threading.stack_size(67108864)

p1 = multiprocessing.Process(target=func1)
p2 = multiprocessing.Process(target=func2)
p1.start()
p2.start()
p1.join()
p2.join()
