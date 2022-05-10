import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 使用pymysql模块连接数据库
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='my_blog', port=3306, charset='utf8')
cursor = conn.cursor()

# 打开文件并读取
f = open('/Users/lidongdong/Desktop/my_blog/my_blog/spiders/data.txt', 'r')
data = f.read()
f.close()

# 将数据插入到数据库中
sql = "insert into blog_article (title, body, created_time, modified_time, excerpt, category_id, author_id) values (%s, %s, %s, %s, %s, %s, %s
