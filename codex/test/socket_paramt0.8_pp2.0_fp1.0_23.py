import socket
socket.if_indextoname()

def find_host():
    try:
        print('\nCoded By: Anuj Patel')
        print('\n\t\t\t[+] Your IP Adress: {}'.format(socket.gethostbyname(socket.gethostname())))
        print('\t\t\t[+] Hostname: {}'.format(socket.gethostname()))
        print('\t\t\t[+] IP Adrress: {}'.format(socket.gethostbyname(socket.gethostname())))
        print('\t\t\t[+] MAC: {}'.format(':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])))
    except Exception as e:
        print('[-] Error: {}'.format(e))

def main():
    find_host()

if __name__ == '__main__':
    main()
