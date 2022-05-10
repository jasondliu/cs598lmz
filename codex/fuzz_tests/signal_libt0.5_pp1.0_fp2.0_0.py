import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def get_number(s):
    if is_number(s):
        return float(s)
    else:
        return 0

def get_number_str(s):
    if is_number(s):
        return s
    else:
        return '0'

def get_number_str_or_none(s):
    if s:
        if is_number(s):
            return s
        else:
            return '0'
    else:
        return '0'

def get_number_or_none(s):
    if s:
        if is_number(s):
            return float(s)
        else:
            return 0
    else:
        return 0

def get_number_or_none_str(s):
    if s:
        if is_number(s):
            return str
