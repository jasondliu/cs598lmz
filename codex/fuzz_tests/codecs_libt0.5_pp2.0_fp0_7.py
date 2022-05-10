import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
def get_connection():
    # 打开数据库连接
    db = pymysql.connect(host='localhost', user='root', passwd='', db='weibo', charset='utf8mb4')
    return db

# 关闭数据库
def close_connection(db):
    db.close()

# 插入数据
def insert(db, table, user_id, screen_name, profile_image_url, profile_url, statuses_count, verified, verified_type, verified_reason, followers_count, follow_count, description, gender, mbrank, mbtype, urank):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql =
