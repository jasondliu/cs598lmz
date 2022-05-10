import threading
threading.active_count
print("Number of active threads:", threading.active_count())


print("\n\n")
t1 = threading.Thread(target=addition)
t2 = threading.Thread(target=multiplication)
t3 = threading.Thread(target=division)
t1.start()
t2.start()
t3.start()
