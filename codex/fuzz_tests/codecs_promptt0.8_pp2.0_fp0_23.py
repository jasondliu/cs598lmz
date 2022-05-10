import codecs
# Test codecs.register_error('myillegal', codecs.UTF8_REPLACE)
# codecs.encode('abc\ufffd', 'utf-8', 'myillegal')
# 'abc\xef\xbf\xbd'

# test #3
import re
# test #3 - remove all illegal characters (except \n and \r)
# codepoints_to_keep = [10, 13]
# pattern = re.compile(u'[^\u%s]' % u''.join([unichr(i) for i in codepoints_to_keep]))
# pattern = re.compile(u'[^\u000A\u000D\u0020-\u007E]')
# pattern = re.compile(u'[^\u000A\u000D\u0020-\u007E\u0081-\u009F]')
# pattern = re.compile(u'[^\u000A\u000D\u0020-\u009F]')
# pattern = re.compile(u'[^\u
