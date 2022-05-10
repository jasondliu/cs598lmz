import codecs
codecs.register_error('strict', codecs.ignore_errors)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False



def is_date(s):
    try:
        datetime.datetime.strptime(s, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def is_month(s):
    try:
        datetime.datetime.strptime(s, "%Y-%m")
        return True
    except ValueError:
        return False

def is_year(s):
    try:
        datetime.datetime.strptime(s, "%Y")
        return True
    except ValueError:
        return False

def is_time_of_day(s):
    try:
        datetime.datetime.strptime(s, "%H:%M:%S")
        return True
    except ValueError:
        return False

def is_month_year(s):
    try:

