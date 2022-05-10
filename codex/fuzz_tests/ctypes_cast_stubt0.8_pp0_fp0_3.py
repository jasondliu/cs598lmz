import ctypes
ctypes.cast(address, ctypes.py_object)


#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((MASTER_IP, MASTER_PORT))
##s.send(bytes(address))
##s.send(str(address))
#d = pickle.dumps(address)
#s.send(d)
#s.close()

#x = "0"

#while x != "1":
#    try:
#        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#        s.connect((MASTER_IP, MASTER_PORT))
#        d = pickle.dumps(address)
#        s.send(d)
#        d = pickle.dumps(apt)
#        s.send(d)
#        d = pickle.dumps(napt)
#        s.send(d)
#        s.close()
#        x = "1"
#    except:
#        time.sleep(10)

