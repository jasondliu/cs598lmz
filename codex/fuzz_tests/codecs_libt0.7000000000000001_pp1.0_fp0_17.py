import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='dianping', charset='utf8mb4')
# 创建游标
cursor = conn.cursor()

cursor.execute(
    'create table if not exists dianping(id VARCHAR(40) NOT NULL, name VARCHAR(40), url VARCHAR(100), url_id VARCHAR(40), PRIMARY KEY (id))')

base_url = 'http://www.dianping.com/search/keyword/7/0_'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

for i in range(0, 50):
    page_url = base_
