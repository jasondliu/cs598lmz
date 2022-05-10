import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='news', charset='utf8mb4')
cursor = conn.cursor()

# 创建索引
def create_index():
    sql = '''
        CREATE TABLE `news_index` (
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `title` varchar(255) NOT NULL,
            `content` text NOT NULL,
            `url` varchar(255) NOT NULL,
            `time` varchar(255) NOT NULL,
            `source` varchar(255) NOT NULL,
            `keywords` varchar(255) NOT NULL,
            `summary` text NOT NULL,
            PRIMARY KEY (`id`)
        ) ENGINE=
