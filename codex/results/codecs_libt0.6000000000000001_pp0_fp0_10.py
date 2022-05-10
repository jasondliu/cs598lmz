import codecs
codecs.open('path', 'r', 'utf-8')

# 正则表达式
import re
match = re.match(r'Hello[ \t]*(.*)world', 'Hello Python world')
match.group(1)
match = re.match(r'/(.*)/(.*)/(.*)', '/user/home/luc')
match.groups()

# 读写json
import json
json.dumps([1, 'simple', 'list'])
json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')

# 时间
from datetime import date
now = date.today()
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
age.days

# 元组
t = 12345, 54321, 'hello!'
t[0
