import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import pymysql.cursors

class Crawler:

	def __init__(self):
		#Database connection configurations
		self.conn = pymysql.connect(host='localhost', user='root', password='', db='crawler', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

	def save_urls(self, urls):
		try:
			with self.conn.cursor() as cursor:
				for url in urls:
					cursor.execute("""INSERT IGNORE INTO `urls` (url) VALUES (%s)""", url)
				self.conn.commit()
		finally:
			#self.conn.close()
			return

	def save_data(self, title, link, content):
		try:
			with self.conn.c
