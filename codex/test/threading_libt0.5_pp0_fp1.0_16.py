import threading
threading.stack_size(1024*1024)

def get_connection():
    return sqlite3.connect(DATABASE, check_same_thread=False)

