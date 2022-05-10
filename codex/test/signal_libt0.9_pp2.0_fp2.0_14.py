import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)  # SIGINT is ignored by default (see:https://stackoverflow.com/q/2795940/3619670)


def get_last_vacuum_date(*args):
    global last_vacuum_date, last_vacuum_date_meta
    last_vacuum_date = _get_last_vacuum_date(*args)
    last_vacuum_date_meta = _get_last_vacuum_date_meta(*args)


def get_vacuum_date_format():
    for i in VACUUM_DATE_FORMATS:
        if i.match(last_vacuum_date):
            return i
    else:
        raise ValueError('{} not in vacuum date format list'.format(last_vacuum_date))


def get_vacuum_position(handler):
    last_vacuum_line_key = '{}_last_vacuum_line'.format(handler)
