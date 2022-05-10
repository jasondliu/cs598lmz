import ctypes
ctypes.windll.shell32.IsUserAnAdmin()

def isUserAdmin():
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True
    else:
        return False

def runAsAdmin(cmdLine=None, wait=True):
    if cmdLine is None:
        cmdLine = []
    elif type(cmdLine) not in (tuple, list):
        raise ValueError('cmdLine is not a sequence')
    cmd = '"{}"'.format(sys.executable)
    if cmdLine:
        cmd += ' ' + ' '.join(cmdLine)
    shell_key = 'SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon'
    with OpenKey(HKEY_LOCAL_MACHINE, shell_key, 0, KEY_READ) as key:
        shell = QueryValueEx(key, 'Shell')[0]
        if isUserAdmin():
            print('I am admin!')
            return run(cmd, wait)
        else:
            print('I am not an admin.')
            return run('
