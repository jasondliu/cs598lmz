import codecs
codecs.open('file', 'r', encoding='utf-8')

# 使用模块
import os
os.listdir('.')

# 安装第三方模块
# pip install Pillow
from PIL import Image
im = Image.open('test.png')
print(im.format, im.size, im.mode)
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')

# 安装第三方模块
# pip install mysqldb
import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='test')
cursor = conn.cursor()
cursor.execute('select * from user')
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()

# 安装第三方模块
# pip install requests
import
