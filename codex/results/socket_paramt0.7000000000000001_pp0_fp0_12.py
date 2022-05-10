import socket
socket.if_indextoname(3)

# solution:
# https://stackoverflow.com/questions/24866131/pypyodbc-unable-to-find-dsn-in-given-dsn-string

import pypyodbc
connection = pypyodbc.connect(driver='{SQL Server}', host='localhost', database='mydb', uid='myuser', pwd='mypass')
cursor = connection.cursor()
</code>

