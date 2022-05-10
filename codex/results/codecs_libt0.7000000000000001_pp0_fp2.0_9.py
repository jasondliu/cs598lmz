import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

config = {
  'user': 'root',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'finance',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

insert_s = ("INSERT INTO user "
               "(u_id,name,gender,weibo_url,weibo_id,city,province,verified_type,description,followers_count,friends_count,statuses_count,favourites_count,created_at,verified_reason) "
               "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

base_url = 'http://weibo.com/'

def get_
