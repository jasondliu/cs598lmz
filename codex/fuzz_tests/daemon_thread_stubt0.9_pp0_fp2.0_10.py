import sys, threading

def run():
    http_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    http_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    http_server.bind((HOST, PORT))
    http_server.listen(10)

    print('web server', HOST, 'port', PORT, 'star')

    while True:
        conn, addr = http_server.accept()

        #print('connect addr', addr)

        #為了防止接收timeout
        conn.settimeout(5)
        try:
            data = conn.recv(1024)
            str = data.decode('utf-8')
            # 利用知道的HTTP服務器的功能，我們可以得知，請求或相關訊息是透過對
