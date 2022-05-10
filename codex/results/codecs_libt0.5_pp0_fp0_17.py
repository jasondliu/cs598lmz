import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='shopping',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Select all Students
        sql = "SELECT * FROM `product`"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()

# # Connect to the database
# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='',
#                              db='shopping',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)

# try:
#    
