import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建数据库连接
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='mysql', charset='utf8mb4')
cur = conn.cursor()
cur.execute("USE wikipedia")

# 创建停用词列表
def get_stop_words():
    stop_words = []
    with open('stop_words.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            stop_words.append(line.strip())
    return stop_words

# 创建停用词表
def create_stop_words_table():
    cur.execute("DROP TABLE IF EXISTS stop_words")
    cur.execute("CREATE TABLE stop_words (id INT PR
