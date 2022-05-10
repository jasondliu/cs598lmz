import bz2
bz2.decompress(bz2.compress(b'Hello World'))

# 1.5 字符串忽略大小写的搜索替换
import re
text = 'UPPER PYTHON, lower python, Mixed Python'
re.findall('python', text, flags=re.IGNORECASE)
re.sub('python', 'snake', text, flags=re.IGNORECASE)

# 1.6 字符串以忽略大小写的方式检查开头或结尾
filename = 'spam.txt'
filename.endswith('.txt')
filename.startswith('file:')
url = 'http://www.python.org'
url.startswith('http:')

# 1.7 用shell通配符匹配字符串
from fnmatch import fnmatch, fnmatchcase
fnmatch
