import threading
threading.stack_size(256 * 1024 * 1024)

from postgre_connect import pg_connect
from tcp_server import Server
from mqtt_client import MQTTClient
import config

"""
Get a new (unique) id of the item using a global variable
"""
id_num = 0
def get_id_num():
    global id_num
    id_num += 1
    return id_num

# Keys for the dictionary's values
MQTTVALUE = "mqtt_value"
ID = "id"
ERROR = "error"

"""
thread-safe function to write to a json file
    - data = the data to write to the file
    - file_fileName = the name of the json file
"""
def safe_write_json(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as jFile:
        json.dump(data, jFile, indent=4)


"""

"""
def read_all_items():
    pgClient = pg_connect()
