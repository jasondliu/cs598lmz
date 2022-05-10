import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# MySQL stuff
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your-password-here'
app.config['MYSQL_DB'] = 'your-db-name-here'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# database object
mysql = MySQL(app)

# database connection
def database_connection():
    conn = mysql.connect()
    # create cursor object
    cursor = conn.cursor()
    return conn, cursor

# database query
def database_query(query):
    # connect to database
    conn, cursor = database_connection()
    # execute the query
    rows = cursor.execute(query)
    # fetch the query result
    data = cursor.fetchall()
    # close connection
    conn.close()
   
