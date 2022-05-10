from lzma import LZMADecompressor
LZMADecompressor().decompress(data).decode('utf-8')

def get_root_pass(data):
    password = get_password(data)
    if password:
        return password
    else:
        return 'root'

def get_password(data):
    if 'root_pass' in data.keys():
        return data['root_pass']
    elif 'root_password' in data.keys():
        return data['root_password']
    else:
        return False

def get_username(data):
    if 'username' in data.keys():
        return data['username']
    else:
        return 'root'

def get_ip(data):
    if 'ip' in data.keys():
        return data['ip']
    else:
        return '0.0.0.0'

def get_port(data):
    if 'port' in data.keys():
        return data['port']
    else:
        return '22'

def get_key(data):
    if 'key' in data.keys():
        return
