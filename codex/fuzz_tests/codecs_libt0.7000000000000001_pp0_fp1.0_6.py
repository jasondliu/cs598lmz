import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='jhy159753',
    db='movie',
    charset='utf8mb4'
)

cursor = conn.cursor()
sql = """
    insert into movie_list(title,url,save_path,score,image_url,m_type,director,actor)
    values(%s,%s,%s,%s,%s,%s,%s,%s)
"""

def insert_db(title,url,save_path,score,image_url,m_type,director,actor):
    try:
        cursor.execute(sql,(title,url,save_path,score,image_url,m_type,director,actor))
        conn.commit()
    except:
        conn.rollback()

def close_db():
    cursor.close()
   
