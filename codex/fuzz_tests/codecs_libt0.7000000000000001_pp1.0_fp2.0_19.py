import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
def get_db():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='jd',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

# 插入商品数据
def insert_data(data):
    # 创建连接
    connection = get_db()
    try:
        with connection.cursor() as cursor:
            # 执行sql语句
            sql = "INSERT INTO `product`(`goods_id`, `goods_name`, `shop_name`, `brand_name`, `category_name`, `jd_price`, `price`, `comments`, `comments_url`, `
