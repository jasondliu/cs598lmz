from bz2 import BZ2Decompressor
BZ2Decompressor
# get data from the mysql server
server_name = "http://yoda.telecomnancy.univ-lorraine.fr"
server_database="db_maville"
server_user="maville_root"
server_pwd="bwtWZqaT"
import mysql.connector
cnx = mysql.connector.connect(user=server_user, password=server_pwd,host=server_name[7:],database=server_database)
cur = cnx.cursor()
get_all_table = "SELECT \
                    TABLE_NAME \
                FROM \
                    INFORMATION_SCHEMA.TABLES \
                WHERE \
                    TABLE_TYPE = 'BASE TABLE' \
                AND \
                    TABLE_SCHEMA=DATABASE() \
                AND \
                    TABLE_NAME LIKE '%_lille' "
get_data_lille = "SELECT * FROM lille_lille"
# SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='lille_lille';
colname_lille = ["
