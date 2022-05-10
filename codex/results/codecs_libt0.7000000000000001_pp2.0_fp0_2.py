import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)


# In[ ]:


db = MySQLdb.connect(host='localhost', user='root', password='', db='movie_data')
cursor = db.cursor()

sql = "INSERT INTO movie_data.movie (title, genre, director, writer, actor, runtime, rating, description, poster_url, imdb_url, type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

for i in range(len(data)):
    cursor.execute(sql, (data[i]['title'], data[i]['genre'], data[i]['director'], data[i]['writer'], data[i]['actor'], data[i]['runtime'], data[i]['rating'], data[i]['description'], data[i]['poster_url'], data[i]['imdb_url'], data[
