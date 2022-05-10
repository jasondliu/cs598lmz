import codecs
codecs.open("myfile.txt", encoding='utf-8')

import io
io.open("myfile.txt", mode='r', encoding='utf-8')

# Disadvantage of UTF-8 is that it can only represent a subset of Unicode,
# but it is by far the most widely used encoding on the web.

# Python 3.0
# string.encode(encoding='UTF-8',errors='strict')
# unicode.encode(encoding='UTF-8',errors='strict')
# bytes.decode(encoding='UTF-8',errors='strict')
# bytes.decode(encoding='UTF-8',errors='replace')
# bytes.decode(encoding='UTF-8',errors='ignore')

# Python 2.7
# string.encode(encoding='UTF-8',errors='strict')
# unicode.encode(encoding='UTF-8',errors='strict')
# str.decode(encoding='UTF-8',errors='strict')
# str.decode(encoding='UTF-8',
