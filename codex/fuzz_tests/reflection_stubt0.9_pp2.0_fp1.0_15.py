fn = lambda: None
gi = (i for i in ())
fn.__code__ = 0
gi.gi_code = 0
</code>
I use Python 2.7 or 3.2.
I am trying to make the following minimalistic example work. I use the <code>ThisWayUp</code> engine.
<code>from cocos.scenes import *
from cocos.layer import *
from cocos.actions import *

from ThisWayUp.twu_skeleton import Play
from ThisWayUp.twu_sceneparser import parse
from ThisWayUp.twu_game import Game

class TestGame(Game):

    def __init__(self, scene=None):
        Game.__init__(self)
        self.scene = scene

    def start(self):
        self.set_scene(self.scene)
        Game.start(self)

    def set_scene(self, scene):
        self.scene.setup(self)

# start scene

sc = parse('''
    - type: label
        text: "Starting game"
    - anykey:
        - go_to: scene1
''')

Game.
