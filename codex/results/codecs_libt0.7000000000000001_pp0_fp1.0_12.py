import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import pymysql
import pymysql.cursors

def connect_to_mysql():
    global conn
    global cursor
    conn = pymysql.connect(host="localhost",user="root",passwd="",db="python_project",charset='utf8mb4',use_unicode=True)
    cursor = conn.cursor()

def disconnect_to_mysql():
    cursor.close()
    conn.close()

def insert_to_database(dt,title,price,old_price,discount,link,image_link,details,category_id,total_page,page_number):
    sql = "INSERT INTO `offers` (`id`, `dt`, `title`, `price`, `old_price`, `discount`, `link`, `image_link`, `details`, `category_id`,`total_page`,`page_number`) VALUES (NULL, %s, %s, %s, %
