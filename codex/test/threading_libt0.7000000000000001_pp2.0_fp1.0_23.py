import threading
threading.Thread(target=my_server).start()
print("Server loop running in thread:", threading.get_ident())

