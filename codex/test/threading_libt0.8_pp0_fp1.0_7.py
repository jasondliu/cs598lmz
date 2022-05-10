import threading
threading.Thread(target=check_for_one_second(5)).start()
threading.Thread(target=check_for_half_second(5)).start()
 
print(a)
