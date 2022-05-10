import threading
threading.stack_size(32768)


HOST = '127.0.0.1'
PORT = 11111

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

msg = []

def printMessages():
  with open('output.txt', 'w') as f:
    data = "\n".join(msg)
    f.write(data)

def sender():
  while True:
    conn, addr = s.accept()
    print('Connected by', addr)
    while 1:
      data = conn.recv(1024)
      # print('got data:', data)
      if not data: 
        msg.append(str(time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())) + " The client has disconnected.")
        break
