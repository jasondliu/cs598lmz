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
        print("θΏζ₯ζε")
    return connect

