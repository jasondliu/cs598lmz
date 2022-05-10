import socket
socket.if_indextoname(3)

# 选择哪个网卡发送数据
s.bind(('127.0.0.1', 8889))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('new conn:', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print('客户端已断开')
            break
        print('执行指令:', data)
        cmd_res = os.popen(data.decode()).read()
        if len(cmd_res) == 0:
            cmd_res = 'cmd has no output....'
        conn.send(str(len(cmd_res.encode())).encode('utf-8'))
        client_ack = conn.recv(1024)
        conn.send(cmd_res.encode('utf-8'))
    conn.close()
s.close()
