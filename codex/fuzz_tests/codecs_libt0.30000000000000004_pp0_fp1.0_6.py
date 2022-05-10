import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 数据库连接
def get_connection():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='123456',
                           db='jd',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

# 获取商品列表
def get_product_list(page):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM product WHERE status = 0 LIMIT %s, %s"
            cursor.execute(sql, (page * 10, 10))
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

# 获取商品详情
def get_product_detail(product
