import mmap
import array
import sqlite3
import sys

dbname = '/project/fas/sbsc/ga254/dataproces/GEOGGMC/GRANAT/data/Granat.db'

# max_lng = maxlon
# min_lng = minlon
# min_lat = minlat
# max_lat  = maxlat

min_lng, min_lat, max_lng, max_lat = 145, 40, 148, 45

# open SQLlite database 
db = sqlite3.connect(dbname)

# open the table of the DB
cur = db.cursor()
sql2 = 'SELECT tiffname FROM GEOGGMC WHERE lat > %s and lat < %s and long > %s and long < %s  ;' %  (min_lat, max_lat, min_lng, max_lng )  
cur.execute(sql2)
# print the tiles intersecting the limits
for row in cur:
    tiffname = row[0]

