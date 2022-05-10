import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _coding(l):
    l = l.rstrip('\r\n')
    if not l:
        return l
    try:
        l = l.decode('utf-8')
    except UnicodeDecodeError:
        l = l.decode('gbk', 'strict')
    return l.encode('utf-8')

def _build_command(command):
    if is_windows:
        return ' '.join(command)
    else:
        return ' '.join(['\'%s\'' % item for item in command])

def _execute(command, stdin=None, cwd=None, env=None):
    if is_windows:
        command = ' '.join(command)
        shell = True
    else:
        command = _build_command(command)
        shell = False

    if stdin:
        stdin = stdin.encode('utf-8')

    log.info('execute:%s' % command)
    try:
        p = subprocess
