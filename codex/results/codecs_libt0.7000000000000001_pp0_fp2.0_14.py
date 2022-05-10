import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='twitter_data',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:

    sql = "SELECT * FROM `tweets` WHERE `tweets`.`tweet_id` = %s"
    cursor.execute(sql, (tweet_id))

    result = cursor.fetchone()
    print(result['tweet_text'])
</code>

