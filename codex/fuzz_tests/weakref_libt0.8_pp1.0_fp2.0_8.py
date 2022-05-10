import weakref

from yyagl.gameobject import LogicColleague
from yyagl.observer import Subject
from yyagl.event import EventDispatcher


class EngNotifier(Subject):

    @property
    def num_players(self):
        return self.args[0]

    @property
    def track_id(self):
        return self.args[0]

    @property
    def is_online(self):
        return self.args[0]

    @property
    def is_alive(self):
        return self.args[0]

    @property
    def is_ai(self):
        return self.args[0]

    @property
    def ai_idx(self):
        return self.args[1]

    @property
    def distrib_idx(self):
        return self.args[0]

    @property
    def distrib(self):
        return self.args[2]

    @property
    def is_valid(self):
        return self.args[0]

    @property
   
