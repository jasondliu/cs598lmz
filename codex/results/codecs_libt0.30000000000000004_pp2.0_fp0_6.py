import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute("USE scraping")

# 获取页面
def get_url(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

# 存入数据库
def insert_db(title):
    cur.execute("INSERT INTO pages (title) VALUES (\"%s\")", (title))
   
