import codecs
codecs.register(lambda n: n is None and codecs.lookup('utf8') or None)

def get_conn():
	return pymysql.connect(
		host='localhost',
		port=3306,
		user='root',
		password='root',
		database='test',
		charset='utf8')
