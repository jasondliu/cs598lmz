import _struct

PORT = 5000           #Port where server listen
LISTEN_LIMIT = 5      #Limit length of queue of connections

class Server:
  def __init__(self, port, listen_limit):
    print ('Initializing server...')
    #initialize socket
    self.server = socket.socket()

    #bind to port
    self.server.bind(('', port))

    #start listening
    self.server.listen(listen_limit)
    print ('Server listening to port: '+str(port))

  def Send(self, msg, conn, addr):
    try:
      conn.send(str.encode(msg))
    except Exception as e:
      print ('Couldnt send MSG:\n'+str(msg))
      print ('Client: '+str(addr))
      print ('Msg type: '+str(type(msg))+'\n')
      raise e

  def Recv(self, conn):
    try:
      return conn.recv(1024).decode()
    except Exception as e:
      print ('Couldnt rec
