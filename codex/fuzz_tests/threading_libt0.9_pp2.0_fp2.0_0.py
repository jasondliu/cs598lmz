import threading
threading.stack_size(6000000)

match = re.compile('^([^\s]+)\s+\|\s+"([^"]+)"\s+(.+)$')
mapping = {
  "R": "Reddit",
  "T": "Twitter",
  "F": "Facebook",
  "Y": "Youtube",
  "G": "Google+"
}

def clear(id):
  mydb = mysql.connector.connect(
    host="aal5w2h53910yu.cosfdv8gfbgl.us-east-1.rds.amazonaws.com",
    user="broughts",
    passwd="furman1825",
    database="broughts"
  )

  mycursor = mydb.cursor()

  sql = "UPDATE comments SET text=NULL, dt=NULL, mapped=NULL WHERE id=" + str(id)

  mycursor.execute(sql)

  mydb.commit()

  mycursor.close()
  mydb.close()

def threads_
