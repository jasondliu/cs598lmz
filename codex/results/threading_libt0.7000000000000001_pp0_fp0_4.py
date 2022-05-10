import threading
threading.Thread(target=s.run, args=(s.sock, s.addr)).start()
s.run(s.sock, s.addr)
#--------------------------------------------------------------------------------------------#

#--------------------------The server receives message from client----------------------------#
def receive(sock):
    msg = ''
    while True:
        char = sock.recv(1).decode()
        if char == '\n':
            break
        else:
            msg += char
    return msg.strip()
#--------------------------------------------------------------------------------------------#

#--------------------------The server checks if the message is valid-------------------------#
def check(msg):
    if msg == 'GAMESTART' or msg == 'GAMEOVER' or msg == 'REPLAY' or msg == 'INVALID' or msg == 'VALID':
        return True
    else:
        return False
#--------------------------------------------------------------------------------------------#

#--------------------------The server processes the message----------------------------------#
def process(sock, msg):
    if check(msg):
        return msg
    elif msg == 'BEGIN':
        sock.send('READY\
