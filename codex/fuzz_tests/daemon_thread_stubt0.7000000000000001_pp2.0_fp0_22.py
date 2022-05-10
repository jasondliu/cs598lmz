import sys, threading

def run():
    global c_socket
    global c_addr
    global c_port
    global c_timeout
    global c_buffer
    global c_buffersize

    print('Connecting to ' + c_addr + ' on port ' + str(c_port) + '...')

    while True:
        try:
            c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            c_socket.connect((c_addr, c_port))
            c_socket.settimeout(c_timeout)
            c_socket.send(c_buffer.encode('UTF-8'))
            c_buffer = c_socket.recv(c_buffersize).decode('UTF-8')
        except Exception as e:
            print('Error occurred: ' + str(e))

        if sys.stdin.isatty():
            print('Input: ' + c_buffer)
        else:
            print(c_buffer)

if __name__ == '__main__':
    if len(sys.argv) < 2:
