import socket
socket.if_indextoname(1)

def connect(user,password,db,hostname,charset):
    connect = pymysql.connect(
        user=user,
        password=password,
        db=db,
        host=hostname,
        charset=charset,
        cursorclass=pymysql.cursors.DictCursor)
    if connect:
        print("连接成功")
    return connect

connect("root","123456","im",socket.gethostbyname("im"),'utf8mb4')
