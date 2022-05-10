import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class GameEngine(object):
    """
    The GameEngine class is responsible for carrying out all the activities
    of the game
    """

    def __init__(self, player, board):
        self.__game_board = board
        self.__player = player
        self.__ai_on = False
        self.__game_over = False
        self.__turn_number = 0
        self.__player.set_letter(board.get_player_letter())

    def get_player_score(self):
        return self.__player.get_total_score()

    def get_player_color(self):
        return self.__player.get_color()

    def get_player_letter(self):
        return self.__player.get_letter()

    def get_turn_number(self):
        return self.__turn_number

    def get_game_board(self):
        return self.__game_board

    def get_ai_on(self):

