import select

class commands():
    def __init__(self,stdscr,game):
        self.stdscr = stdscr
        self.game = game
        self.cmds = {
                'h': self.move_player_left,
                'j': self.move_player_down,
                'k': self.move_player_up,
                'l': self.move_player_right,
                'y': self.move_player_upleft,
                'u': self.move_player_upright,
                'b': self.move_player_downleft,
                'n': self.move_player_downright,
                'i': self.open_inventory,
                'I': self.open_inventory,
                'x': self.open_equipment,
                'X': self.open_equipment,
                'Q': self.quit_game,
                'q': self.quit_game,
                's': self.save_game,
                'S': self.save_game,
                'g': self.pickup_item
