import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

#数据库连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='root',
    db='douban',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# 创建游标
cur = conn.cursor()

#设置请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Host": "movie.douban.com"
}

#获取总页数
def
