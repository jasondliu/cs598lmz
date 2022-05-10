import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 主函数
def main():
    mongo = MongoClient('localhost', 27017)
    db = mongo['spider_db']
    collection = db['spider_collection']
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute("SELECT * FROM weibo")
    # 使用 fetchone() 方法获取一条数据库。
    data = cursor.fetchall()
    print("Database version : %s" % data)
    # 关闭数据库连接
    db.close()

if __name__ == '__main__':
    main()
