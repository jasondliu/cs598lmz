import socket
import ssl


def get_text_from_ssl_socket(url, host, port, https, username, password):
    if https:
        context = ssl.create_default_context()
        sock = socket.create_connection((host, port))
        connection = context.wrap_socket(sock, server_hostname=host)
    else:
        connection = socket.create_connection((host, port))

    connection.settimeout(10.0)

    try:
        connection.send(b'GET %s HTTP/1.0\r\nHost: %s\r\n'
                        b'\r\n' % (url.encode('utf-8'), host.encode('utf-8')))
    except socket.error as error:
        return False, str(error)

    buf = connection.recv(1024)
    response = buf.decode()

    if response.split()[1] != '200':
        return False, response

    ok = True
