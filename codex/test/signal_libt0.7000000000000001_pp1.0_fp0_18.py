import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)


class DieCond(Condition):
    def __init__(self, zomb=False):
        super(DieCond, self).__init__()
        self.zomb = zomb

    def check(self, entities):
        for ent in self.filter_entities(entities):
            if ent.hp <= 0:
                if ent.zomb:
                    ent.zomb = False
                    ent.hp = 1
                    ent.player_controlled = True
                else:
                    ent.destroy()
                return True


class AICond(Condition):
    def __init__(self, ai, zomb=False):
        super(AICond, self).__init__()
        self.ai = ai
        self.zomb = zomb

    def check(self, entities):
        for ent in self.filter_entities(entities):
            if not isinstance(ent, PlayerEnt):
                if self.zomb and not ent.zomb:
                    continue
                self
