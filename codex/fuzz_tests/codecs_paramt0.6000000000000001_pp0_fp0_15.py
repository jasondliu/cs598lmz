import codecs
codecs.register_error('skip', lambda _, x: (b'', x.start + 1))

def parse_line(line):
    try:
        ip, ident, user, time = re.split(r'\s+', line, 3)
        time = time[1:]
        return ip, ident, user, time
    except ValueError:
        return None, None, None, None

def parse_time(time):
    try:
        return time[1:-1]
    except IndexError:
        return None

def parse_url(url):
    try:
        return re.split(r'\s+', url, 1)[0]
    except IndexError:
        return None

def parse_status_code(status_code):
    try:
        return int(status_code)
    except ValueError:
        return None

def parse_bytes(bytes):
    try:
        return int(bytes)
    except ValueError:
        return 0

def parse_logfile(path):
    with open(path, 'rb') as f:
        return (
