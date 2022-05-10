import threading
threading.stack_size(67108864)

t = threading.Thread()
t.start_new_thread(test2,())
t.start_new_thread(test1,())
