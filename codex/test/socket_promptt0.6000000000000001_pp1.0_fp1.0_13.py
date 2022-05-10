import socket
# Test socket.if_indextoname function

def get_hostname_from_ip(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return None

if __name__ == '__main__':
    print(get_hostname_from_ip('192.168.1.1'))
    print(get_hostname_from_ip('8.8.8.8'))
    print(get_hostname_from_ip('127.0.0.1'))
    print(get_hostname_from_ip('192.168.1.100'))
    print(get_hostname_from_ip('192.168.1.101'))
    print(get_hostname_from_ip('192.168.1.102'))
    print(get_hostname_from_ip('192.168.1.103'))
    print(get_hostname_from_ip('192.168.1.104'))
    print(get_hostname_from_ip('192.168.1.105'))
