import threading
threading.Thread().start_new_thread(start_server, (lambda x: None, lambda x: None,))
start_server(lambda x: None, lambda x: None)
