import sys, threading

def run():
    m_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    m_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        m_socket.bind(("0.0.0.0", 9999))
    except Exception:
         sys.exit(1)

    m_socket.listen(10)
    while True:
        conn, addr = m_socket.accept()
        print(conn)
        new_thread = threading.Thread(target=handle_request, args=(conn, addr))
        new_thread.start()
        new_thread.join()


def send(conn, msg):
    conn.send(msg)


def handle_request(conn, addr):
    #conn.send("hello world")
    #data = conn.recv(10240)
    #print(data)
    #time.sleep(1)
    #send(conn, data)
    conn.send("hello world")


if __name__
