import codecs
codecs.register_error('surrogate_escape', codecs.surrogateescape_error)

import winreg

def get_desktop():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
        return winreg.QueryValueEx(key, "Desktop")[0]
    except:
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))

def get_data_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))

def convert_bytes_to_format(bytes, use_MB=True, use_GB=True, use_TB=True, use_PB=True):
    m = 1024.0 ** 2
    mb = m
    g = m * 1024.0
    gb = g
    t = g * 1024.0
   
