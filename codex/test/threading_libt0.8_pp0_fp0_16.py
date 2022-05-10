import threading
threading.current_thread().name

from time import time, ctime, sleep

# 文件过滤函数
def file_filter(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        lines_data = [i for i in lines if i != '\n' and i != '\r\n']
        return lines_data

# 写入文件函数
def write_to_file(new_file_path, file_data):
    with open(new_file_path, 'a', encoding='utf-8') as f:
        f.write('\n'.join(file_data))
        f.write('\n')

# 获得文件数据函数
def get_file_data(file_path, new_file_path):
    start = time()
    print('start %s' % threading.current_thread().name)
    write
