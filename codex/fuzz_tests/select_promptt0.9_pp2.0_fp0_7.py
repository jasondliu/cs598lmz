import select
# Test select.select(W,X,Y,Z)
# W: wait for writing *W will be a list of sockets ready for write
# X: wait for error *X will be a list of sockets with error condition
# Y: wait for reading *Y will be a list of sockets ready for read
# Z is no use

def command_interpreter(connection_socket):
    while True:
        message = connection_socket.recv(4096)
        reply = ''
        if message.startswith('PING'):
            reply = 'PING reply\r\n'
        elif message.startswith('STORE'):
            reply = 'STORE reply\r\n'
        elif message.startswith('RETRIEVE'):
            reply = 'RETRIEVE reply\r\n'
        elif message.startswith('delete'):
            reply = 'delete reply\r\n'
        elif message.startswith('list'):
            reply = 'list reply\r\n'
        elif message.startswith('QUIT'):

