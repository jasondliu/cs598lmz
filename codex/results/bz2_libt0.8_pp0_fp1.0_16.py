import bz2
bz2.BZ2File(path)

# Regular expressions
pattern = 'foo'
re.compile(pattern)

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

re.findall(r'\d+/\d+/\d+', text1)
re.findall(r'\d+/\d+/\d+', text2)

datepat = re.compile(r'\d+/\d+/\d+')
datepat.findall(text1)
datepat.findall(text2)

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat.findall(text)

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
m.group(0)
m.group(1)
m.group(2)
m.group(3)
m.groups()
month, day, year = m.groups()


