import select
# Test select.select()

def accept(s, server_channel):
    client_channel, addr = s.accept()
    print("Server:  Connection from", addr)

    while True:
        yield ('recv', client_channel)
        msg = client_channel.recv(4096)

        if not msg:
            break
        else:
            print("Server:  ", msg.decode('utf-8'))
        yield ('send', client_channel)
        client_channel.send(b'Got:  ' + msg)

    print("Server:  Closing")
    client_channel.close()
    server_channel.close()

import asyncio
loop = asyncio.get_event_loop()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
s.bind(('localhost', 16000))
s.listen(5)
s.setblocking(False)

