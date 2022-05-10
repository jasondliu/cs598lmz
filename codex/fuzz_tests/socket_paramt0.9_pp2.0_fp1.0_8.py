import socket
socket.if_indextoname(1)

# Import and initiate database access
from database import Database
config = json.load(open("/Users/john/tarok/database.conf"))
db = Database(config["database"])

# Select nodes

sql = "SELECT nodeid, nodeid||' '||nodename||' '||netaddress||' '||comment FROM connections"
sql += " JOIN nodes ON connections.nodeid = nodes.nodeid"
sql += " WHERE pid = %s AND netssid = %s"
sql += " ORDER BY nodeid"

d = db.query(sql, (33, 3))
nodes = [{"data":d[i], "rowid":i} for i in range(0, len(d))]

# Select sensors

sql = "SELECT sensorid, nodename||' '||sensorname||' '||comment FROM connections"
sql += " JOIN nodes ON connections.nodeid = nodes.nodeid"
sql += " WHERE pid = %s AND netssid = %s"
sql += " ORDER BY sensorid"

d = db.query
