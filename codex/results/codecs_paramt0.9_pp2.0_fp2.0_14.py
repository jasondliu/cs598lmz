import codecs
codecs.register_error('ignore', codecs.lookup('iso8859-1'))

in_file = sys.argv[1]

html_parser = html.parser.HTMLParser()

def parse_date(text, idate):
    # 15-Oct-2016  12:00 AM

    if 'today' in text or 'gisteren' in text:
        return idate

    if '-' in text:
        fmt = "%d-%b-%Y %I:%M %p"
    else:
        fmt = "%d %b %Y %I:%M %p"
    date = datetime.datetime.strptime(text, fmt)
    date = date.replace(year=idate.year)
    if date < idate:
        date = date.replace(year=idate.year+1)
    if date < idate:
        date = date.replace(year=idate.year-1)
    if date < idate:
        raise Exception('Could not parse date')
    return date

with codecs.open(in_file, 'r',
