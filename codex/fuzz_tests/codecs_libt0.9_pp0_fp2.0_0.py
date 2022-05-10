import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
 
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Sa19980102', db='news', charset='utf8mb4')
cur = conn.cursor()

sql = "select nContent from news_copy where Id=10;"
result = cur.execute(sql)
news_content= cur.fetchone()[0]
print news_content

reload(sys)
sys.setdefaultencoding('utf-8')

seg_list = jieba.cut(news_content, cut_all=False)
print seg_list

import jieba.analyse
tags = jieba.analyse.extract_tags(news_content, topK=100, withWeight=False, allowPOS=())
print '|'.join(tags)
