import threading
threading.stack_size(10*1024*1024)

global_client_id = 0
global_player_id = 0
global_multi_player_flag = 0
global_multi_player_lock = threading.Lock()

global_multi_player_client_ip = {}


class GamePlay(threading.Thread):
    """This class is called whenever a new game is started"""
    def __init__(self, data, client_id, player_id, ips):
        threading.Thread.__init__(self)
        self.data_str = data
        self.client_id = client_id
        self.player_id = player_id
        self.ips = ips

    def run(self):
        global global_client_id
        global global_player_id
        global global_multi_player_flag
        global global_multi_player_lock
        global global_multi_player_client_id
        global global_multi_player_client_ip


        # print "data", data_json

