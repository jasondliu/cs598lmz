import threading
threading.Thread(target=echoServer, args=(6001,)).start()
# wait for incoming requests
import socket
print('The server is waiting for incoming requests!')
import time
time.sleep(50)
tcpClntSock.close()
