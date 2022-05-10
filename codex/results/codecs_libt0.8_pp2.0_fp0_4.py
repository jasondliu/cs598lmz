import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

connection = pymysql.connect(host='localhost',
                            user='root',
                            password='1314520',
                            db='business',
                            port=3306,
                            charset='utf8mb4')

def select(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    # if results == None:
    #     return 0
    return results


def get_ids():
    sql = 'select id from business_shop'
    results = select(sql)
    return results


def get_shop_info(id):
    sql = 'select * from business_shop where shop_id={0}'.format(id)
    results = select(sql)
    return results[0]


def get_goods_info(id):
    sql = 'select * from business_goods where shop_id={0}'.format(id)
    results
