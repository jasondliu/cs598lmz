import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class block(QGraphicsRectItem):
    def __init__(self, r):
        super().__init__(r)

class texture(QPixmap):
    def __init__(self, path):
        super().__init__(path)
        
class player(QGraphicsPixmapItem):
    def __init__(self, texture):
        super().__init__(texture)
        
class Game(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.main_game = 0
        
        self.main_scene = QGraphicsScene(0, 0, 640, 480)
        self.setScene(self.main_scene)
        
        self.load_textures()
        
        self.main_player = player(self.player_texture)
        
        self.main_scene.addItem(self.main_player)
        
    def build_main_game(self):
        self.main_game =
