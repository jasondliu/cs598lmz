import threading
threading.stack_size(1024**2)

import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

WORKSPACE = os.environ.get('WORKSPACE_PATH').replace('/nfs/user/guitar79/PycharmProjects/remote_sensing', '', 1)

from core import sensing_data

# Import 한 모듈을 이용하여 시간 계산
# time check
import time
start_time = time.time()

def get_files(base_dir, file_name, date):
    import glob
    import datetime
    file_list = []
    if date[-2:] == '00':
        date_stamp = time.mktime(datetime.datetime(int(date[:4]), int(date[4:6]), int(date[6:8]), 23).timetuple())
    else:
