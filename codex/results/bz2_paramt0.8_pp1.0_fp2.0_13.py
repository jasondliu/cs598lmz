from bz2 import BZ2Decompressor
BZ2Decompressor


# In[ ]:


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)
 
    return None


# In[ ]:


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        print(e)


# In[ ]:


def get_data(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
        data = c.fetchall()
        return data
    except Exception as e:
        print(e)


# In[ ]:


def main():
    file = 'data/Sensors/sensors.db'
    sql_create_sensors = """ CREATE TABLE IF NOT EXISTS sensors (
                                        record_id integer PRIMARY KEY,
                                        temperature real,
                                       
