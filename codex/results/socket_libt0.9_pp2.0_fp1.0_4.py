import socket
host = 'localhost'
socket1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket1.bind((host,25252))
socket1.listen(1)

def main():
    x=0
    temp=''
    data1=''
    data=''
    s=''
    global host
    print('\nSocket created')
    #print(host)
    for i in range (0,3):
        conn,addr=socket1.accept()
        print('\nConnected to ',addr[0],addr[1])
        #print('recv1',conn.recv(100))
        while True:
            data=conn.recv(100)
            #print(data)
            if data!='':
                print(data)
                if 'filename' in data:
                    data=data[8:]
                    print('\n',data)
                    conn.sendall(b'OK,1')
                    #data=[]
                elif 'data2' in data:
                    print('\n
