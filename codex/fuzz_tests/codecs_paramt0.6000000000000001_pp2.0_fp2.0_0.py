import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_config():
    if os.path.exists(os.path.join(os.path.dirname(__file__), 'config.py')):
        return config
    else:
        return config_template

def get_user():
    return get_config()['user']

def get_password():
    return get_config()['password']

def get_index_url():
    return get_config()['index_url']

def get_login_url():
    return get_config()['login_url']

def get_session_file():
    return get_config()['session_file']

def get_cookies():
    if not os.path.exists(get_session_file()):
        return {}
    f = open(get_session_file(), 'r')
    r = f.read()
    f.close()
    return pickle.loads(r)

def save_cookies(cookies):
    r = pickle.dumps(cookies)

