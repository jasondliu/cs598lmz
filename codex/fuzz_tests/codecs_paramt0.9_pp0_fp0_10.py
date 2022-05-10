import codecs
codecs.register_error('replace_with_space', codecs.replace_with(u'/', u' '))

# unicode cleaner
def clean(text):
    if text is None:
        return
    text = text.strip()
    text = text.replace('<br>', '\n')
    text = unescape(text)
    return text.encode('utf-8')

# check for valid data
def valid(row):
    if row == None:
        return False
    if row == u'':
        return False
    if row == '':
        return False
    return True

# print a row
def print_row(row):
    if valid(row[0]):
        print clean(row[0])
    if valid(row[1]):
        print clean(row[1])
    if valid(row[2]):
        print clean(row[2])
    if valid(row[3]):
        print clean(row[3])
    if valid(row[4]):
        print clean(row[4])
    if valid(row[5
