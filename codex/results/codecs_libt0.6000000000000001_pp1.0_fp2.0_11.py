import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

class ChessPgn:
    """
    A class that reads a pgn file and can return games as a list of moves or as a board.
    """
    def __init__(self, file_name):
        self.file_name = file_name
        self.game_count = 0
        self.white_wins = 0
        self.black_wins = 0
        self.draws = 0
        self.game_index = 0
        self.games = []
        self.game_file = open(self.file_name, 'r')
        self.build_game_list()
        self.game_file.close()

    def build_game_list(self):
        """
        Builds a list of games from the pgn file.
        :return:
        """
        cur_game = []
        for line in self.game_file:
            if line.startswith('[Result'):
                result = line.split()
