import socket
socket.if_indextoname(3)


def display_hostname_service(host, service):
    print("Host:", host, "Service:", str(service))

def test_host_service(host, service):
    try:
        name = socket.gethostbyaddr(host)
        display_hostname_service(name[0], service)
    except socket.error as msg:
        print("ERROR:", msg)
    except socket.gaierror as msg:
        print("ERROR: Name service failure:", msg)
    except socket.herror as msg:
        print("ERROR: Host service failure:", msg)

test_host_service('192.168.1.1',80)
test_host_service('www.doughellmann.com',80)
test_host_service('192.168.1.1','http')
test_host_service('www.doughellmann.com','http')
