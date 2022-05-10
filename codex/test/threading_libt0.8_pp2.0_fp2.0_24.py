import threading
threading.stack_size(67108864) 


class Synchronizer(threading.Thread):
    """ Thread used to synchronize the mission manager and the SCRIMMAGE commander """
    def __init__(self, mission_manager, connect_to_scrimmage, port=1337, host='127.0.0.1'):
        threading.Thread.__init__(self)
        self.initialized = False
        self.mission_manager = mission_manager
        self.manager_commander = mission_manager.commander
        self.port = port
        self.host = host
        self.is_running = False
        self.skt = None
        self.skt_lock = threading.Lock()
        self.skt_connected = False
        self.skt_condition = threading.Condition()
        self.connect_to_scrimmage = connect_to_scrimmage
        self.connect_to_scrimmage_lock = threading.Lock()

