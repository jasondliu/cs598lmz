import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='root', db='mysql', charset='utf8mb4')
curs = conn.cursor()

# 불러온 데이터를 넣을 리스트
title_list = []
contents_list = []

# 크롤링할 웹페이지 주소
url = 'http://www.dogdrip.net/index.php?mid=free&page=1&document_srl=1648650'

# 크롤링할 웹페이지 주소를 읽어온다.
html = urlopen(url)

