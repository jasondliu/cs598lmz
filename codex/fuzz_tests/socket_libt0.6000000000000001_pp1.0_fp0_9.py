import socket, pickle

def main():
    host='127.0.0.1'
    port=5050

    s=socket.socket()
    s.bind((host,port))
    s.listen(1)
    c,addr=s.accept()
    print("Connection from: " + str(addr))
    while True:
        data=c.recv(1024)
        if not data:
            break
        print("From connected user: " + str(data))
        data=str(data).upper()
        print("Sending: " + str(data))
        c.send(data)
    c.close()

if __name__ == '__main__':
    main()
</code>


A:

It's because you're trying to send a string.  You need to serialize the objects first.  The easiest way to do this is to use <code>pickle</code>:
<code>import pickle

# ...

data = pickle.dumps(data)
</code>

