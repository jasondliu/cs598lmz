import socket
# Test socket.if_indextoname()

def get_if_indextoname():
    print([socket.if_indextoname(i) for i in range(10)])

def get_if_indextoname_error():
    try:
        print(socket.if_indextoname(1))
    except socket.error as e:
        print(e)

def get_if_indextoname_error2():
    try:
        print(socket.if_indextoname(1))
    except socket.error as e:
        print(e.args)

def get_if_indextoname_error3():
    try:
        print(socket.if_indextoname(1))
    except socket.error as e:
        print(e.args[0])

if __name__ == '__main__':
    get_if_indextoname()
    get_if_indextoname_error()
    get_if_indextoname_error2()
    get_if_indextoname_error3()
