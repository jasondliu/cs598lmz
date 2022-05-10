import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
try:
    import MySQLdb.cursors
except ImportError:
    mysqlclient = False
else:
    mysqlclient = True
import math
import spacy
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer

#表格
ws = Workbook()
ws.guess_types = True
ws.encoding = 'utf-8'

#添加一个sheet
ws.add_sheet('sheet1')


#Connet to database
if mysqlclient:
    db = MySQLdb.connect(user="root", passwd="1q2w3e4r", db="papers", use_unicode=True, charset="utf8", cursorclass=MySQLdb.cursors.DictCursor)
else:
    db = pymysql.connect(user="root", passwd="1q2w3e4r", db="papers", use_unicode=True,
