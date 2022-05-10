import socket

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def get_mac():
    mac_num = hex(uuid.getnode()).replace('0x', '').upper()
    mac = '-'.join(mac_num[i : i + 2] for i in range(0, 11, 2))
    return mac

def get_hostname():
    return socket.gethostname()

def get_user():
    return getpass.getuser()

def get_os():
    return platform.system()

def get_cpu():
    return platform.processor()

def get_ram():
    return str(round(psutil.virtual_memory().total
