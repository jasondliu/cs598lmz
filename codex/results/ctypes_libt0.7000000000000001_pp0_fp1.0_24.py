import ctypes
ctypes.windll.shell32.IsUserAnAdmin()

# 用户权限
if os.name is 'nt' and not ctypes.windll.shell32.IsUserAnAdmin():
    # ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    sys.exit()

def get_config():
    return read_config(os.path.join(os.path.dirname(__file__), 'config.yaml'))

def get_url(config):
    return "%s/%s" % (config['server'], config['api'])

def get_request(config):
    request = Request(get_url(config))
    request.add_header("Authorization", config['token'])
    return request

def get_response(request):
    try:
        response = urlopen(request)
        return response.read()
    except URLError:
        return None

def get_ip():
    ret = get_response
