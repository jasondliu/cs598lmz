import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

#
# Now we define the main body of our program.
#

# First, we open a connection to the database, and create a cursor to send
# queries to the database.
db = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="TMD")
cur = db.cursor(MySQLdb.cursors.DictCursor)

# We will be using the following functions to build up our database. 

# add_user adds a user to the database. It takes a username, password, and
# an email address.
def add_user(username, password, email):
    cur.execute("INSERT INTO User VALUES(NULL, %s, %s, %s)", (username, password, email))

# add_movie adds a movie to the database. It takes a title, year, and rating.
