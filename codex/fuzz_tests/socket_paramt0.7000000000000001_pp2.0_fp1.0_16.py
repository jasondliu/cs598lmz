import socket
socket.if_indextoname(1)
#'en0'

#查看某个端口是否被占用
import socket
def test_server(address, port):
    s = socket.socket()
    print("Attempting to connect to {} on port {}".format(address, port))
    try:
        s.connect((address, port))
        print("Connected to {} on port {}".format(address, port))
        return True
    except socket.error as e:
        print("Connection to {} on port {} failed: {}".format(address, port, e))
        return False

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Test for a socket')
    parser.add_argument('--host', action="store", dest="host", default="localhost")
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    host = given_args.host
    port
