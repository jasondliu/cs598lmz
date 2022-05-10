import ctypes
import ctypes.util
import threading
import sqlite3
import uuid


log = logging.getLogger(__name__)

db_lock = threading.Lock()


class IMRData(object):

    def __init__(self, data, timestamp, sequence_number):
        self.data = data
        self.timestamp = timestamp
        self.sequence_number = sequence_number


class ImrClient(object):

    def __init__(self, db_path, imr_url, imr_port):
        self.db_path = db_path
        self.imr_url = imr_url
        self.imr_port = imr_port
        self.imr_client_id = str(uuid.uuid1())

    def _process_data(self, data):
        data_list = data.split('\n')

        if len(data_list) > 0:
            data_list = list(filter(None, data_list))

            for data in data_list:
                data_obj = json.loads(data)
