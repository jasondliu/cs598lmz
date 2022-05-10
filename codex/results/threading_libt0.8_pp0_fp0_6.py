import threading
threading.stack_size(1024000)

class peer():
    # Thread-safe counter
    counter = 0
    # Shared variable
    graph = nx.Graph()
    # Thread-safe variable
    is_finished = False
    # Thread-safe variable
    is_leader = False
    # Thread-safe variable
    num_votes = 0
    # Thread-safe variable
    last_leader = None
    # Dictionary containing "leader": timestamp
    last_leader_dict = {}

    def __init__(self, port, master_ip, master_port):
        self.ip = self.get_ip()
        self.port = port
        self.master_ip = master_ip
        self.master_port = master_port
        self.server_process = threading.Thread(target=self.start_server, daemon=True)
        self.server_process.start()
        self.client_process = threading.Thread(target=self.start_client, daemon=True)
        self.client_process.start()
        self.election_process = threading.Thread
