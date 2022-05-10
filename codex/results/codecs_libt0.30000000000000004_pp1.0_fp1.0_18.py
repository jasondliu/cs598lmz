import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='mysql', charset='utf8mb4')
cur = conn.cursor()
cur.execute('USE scraping')

# 创建数据库
def create_database():
    cur.execute('CREATE DATABASE IF NOT EXISTS scraping')
    cur.execute('USE scraping')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS pages (
            id INTEGER PRIMARY KEY AUTO_INCREMENT,
            title VARCHAR(255) UNIQUE,
            content TEXT
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS links (
            from_page_id INTEGER,
            to_page_id INTEGER
