import codecs
codecs.register_error('strict', codecs.ignore_errors)

# from http://stackoverflow.com/questions/4130922/how-to-increment-datetime-month-in-python
def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)

def get_date_from_filename(filename):
    return datetime.datetime.strptime(filename[-14:-4], '%Y%m%d').date()

def get_date_from_filename_old(filename):
    return datetime.datetime.strptime(filename[-10:-4], '%Y%m').date()

def get_date_from_filename_new(filename):
    return datetime.datetime.strptime(filename[-14:-4], '%Y%m%d').
