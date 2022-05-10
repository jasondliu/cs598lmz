import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# 
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
# 
# import sys
# import codecs
# sys.stdout = codecs.getwriter('utf8')(sys.stdout)
# sys.stderr = codecs.getwriter('utf8')(sys.stderr)
# 
# import sys
# sys.setdefaultencoding('utf-8')
# 
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")
# 
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
# 
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
# 
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
# 
# import sys
# reload(sys)
# sys.setdefaultencoding('utf
