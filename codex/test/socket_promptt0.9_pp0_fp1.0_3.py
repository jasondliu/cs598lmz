import socket
# Test socket.if_indextoname()
def testsocket():

    print(socket.getfqdn('24.21.209.82'))
    print(socket.gethostbyname('ec2-3-23-157-138.us-east-2.compute.amazonaws.com'))
    # print(socket.gethostbyname_ex('ec2-3-23-157-138.us-east-2.compute.amazonaws.com'))
    # print(socket.gethostbyaddr('18.236.217.160'))
    # print(socket.getnameinfo())
    # print(socket.if_indextoname())
    # print(socket.if_nametoindex())

if __name__ == "__main__":
    testsocket()
