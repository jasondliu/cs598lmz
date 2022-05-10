import select
# Test select.select()

def test_select(test_objects, test_data):
    test_data = test_objects.get_data(test_data)
    test_data.start()
    test_data.start_threads()
    test_data.start_processes()
    test_data.start_servers()
    
    test_data.init_select(0.01)

    for i in range(0, 100):
        try:
            select.select(test_data.read_list, test_data.write_list, test_data.error_list, 0.01)
        except (select.error, IOError, OSError):
            pass
    
    test_data.stop_servers()
    test_data.stop_processes()
    test_data.stop_threads()
    test_data.stop()
