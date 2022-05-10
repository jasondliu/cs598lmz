import lzma
lzma.LZMAFile

class Dir(object):
    def __init__(self,raw_dir_data):
        self._raw_data = raw_dir_data
        raw_entries = raw_dir_data['entries']
        # print("Raw entries is %s"%(raw_entries))
        self.entries = [GameInfo(raw_entry) for raw_entry in raw_entries]
        # print("First entry is %s"%(self.entries[0]))
    def __str__(self):
        return("Dir:%s"%(pprint.pformat(self._raw_data)))

class GameInfo(object):
    def __init__(self,raw_game_info):
        self._raw_data = raw_game_info
        # print("Really raw game info is %s"%(self._raw_data))
        self.game = Game(self._raw_data['game_data'])
        self.box_art = self._raw_data['box_art']
        self.tags = self._
