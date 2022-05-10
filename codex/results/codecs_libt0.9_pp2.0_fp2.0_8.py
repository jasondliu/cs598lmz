import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

config ={
'user':'root',
'password':'19951103',
'host':'127.0.0.1',
'database':'OS_Project',
'raise_on_warnings': True,
}

def Insert(search):
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()

	add_search = ("INSERT INTO recommend_word" 
    	           "(word)"
        	       "VALUES (%s)")
	data_search = search
	cursor.execute(add_search,data_search)
	cursor.close()
	cnx.commit()
	cnx.close()
	return 0

searchNum = 0
def Find(search):
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()
	find_search = ("SELECT COUNT(*) FROM recommend_word WHERE word
