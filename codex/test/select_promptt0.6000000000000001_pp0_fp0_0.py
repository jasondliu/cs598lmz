import select
# Test select.select
def test_select():
    conn_list = []
    read_list = []
    write_list = []
    error_list = []
    timeout = 10
    ret = select.select(read_list, write_list, error_list, timeout)
