import select
# Test select.select wait for a connection and a message

listener = socket(AF_INET, SOCK_STREAM)
listener.bind(('', 12345))
listener.listen(1)
listener.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
listener.setblocking(0)
print('Listening on port %d' % listener.getsockname()[1])

while True:
    try:
        print('Waiting for connection...')
        (connection, address) = listener.accept()
        connection.setblocking(0)
        print('Got connection from %s' % (address,))

        while True:
            try:
                message = connection.recv(512)
            except BlockingIOError:
                continue

            if not message:
                break

            print(message)

    except KeyboardInterrupt:
        print('Ctrl-C pressed.')
        break

    except Exception as e:
        print('Exception: %s' % (e,))
        continue

