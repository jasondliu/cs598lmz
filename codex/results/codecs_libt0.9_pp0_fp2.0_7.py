import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
os.chdir('/home/mrcode_w')
#login 数据库
conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='blog',charset='utf8')
cur=conn.cursor()

#每页条目
number=10

def get_title(id):
	link="SELECT `title` FROM `article` WHERE id="+str(id)
	cur.execute(link)
	return cur.fetchall()

def get_name(id):
	link="SELECT `author` FROM `article` WHERE id="+str(id)
	cur.execute(link)
	return cur.fetchall()

def getlist(first,last):
	link="SELECT * FROM `article` WHERE  id>"+str(first)+" and id<="+str(last)+"order by id desc"
	
