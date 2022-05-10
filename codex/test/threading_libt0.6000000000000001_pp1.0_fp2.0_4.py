import threading
threading.Thread(target=main,args=(1,)).start()
threading.Thread(target=main,args=(2,)).start()
while True:
	pass
"""
threading.Thread(target=main,args=(1,)).start()
threading.Thread(target=main,args=(2,)).start()
threading.Thread(target=main,args=(3,)).start()
threading.Thread(target=main,args=(4,)).start()
"""
