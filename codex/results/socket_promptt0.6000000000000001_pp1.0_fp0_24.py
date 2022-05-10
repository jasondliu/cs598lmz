import socket
# Test socket.if_indextoname()

def get_interface_list():
    interface_list = []
    for i in range(0, 1024):
        try:
            interface_list.append(socket.if_indextoname(i))
        except:
            pass
    return interface_list

def main():
    interface_list = get_interface_list()
    for interface in interface_list:
        print(interface)

if __name__ == "__main__":
    main()
