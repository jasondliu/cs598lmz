import threading
threading.Thread()
threading.Thread(target=lambda: print("test2"))

s = "test3"
threading.Thread(target=lambda: print(s))

s = "test4"
threading.Thread(target=lambda: print(s))

threading.Thread(target=print, args=["test5"])
threading
