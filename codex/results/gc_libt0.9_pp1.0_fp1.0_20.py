import gc, weakref

class BoLaneMetaClass(type):

    def __new__(meta, classname, supers, classdict):
        if classname != 'BoLane':
            print('Running __new__ with {}'.format(classdict.keys()))

        print( "Creating a Foo", meta, classname, supers, classdict)
        return type.__new__(meta, classname, supers, classdict)


class BoLane(object):
    """
    BoLane

    A class for lanes in boilover

    """

    def __init__(self, name, game, parent, direction="vertical", laneNumber=1, px=None, py=200):
        self.name = name
        self.game = game
        self.parent = parent
        self.direction = direction
        # self.auto_schedule()
        self._handle = 0
        self._has_valid_handle = False
        self.px = px
        self.py = py
        # self.node = self._make_widget()
        self.node = None

    def __str
