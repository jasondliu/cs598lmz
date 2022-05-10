import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

# check if there is an active internet connection
def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

def main():
    # variables
    global is_connected
    global conn
    global cur
    global db
    global db_path
    global is_db_created
    global is_db_connected
    global is_db_table_created
    global is_db_table_connected
    global is_db_table_rows_added
    global is_db_table_rows_removed
    global is_db_table_rows_updated
    global is_db_table_rows_searched
    global is_db_table_rows_displayed
    global is_db_table_rows_dropped
    global is_db_table_dropped
    global is_db_closed
