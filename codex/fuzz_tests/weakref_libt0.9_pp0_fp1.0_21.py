import weakref

from item import Item
from playeritem import PlayerItem
from graphic import Graphic


class Mob(Graphic, Item):
    """A mob with the following characteristics."""
    name = "mob"
    plural = "mobs"
    desc = "a sample mob"
    properties = collections.defaultdict(lambda: None)

    #: float; speed at which the mob moves
    walk_speed = 1.0

    #: callable; function to call when harvesting the mob
    harvest_func = None

    #: pyglet.graphics.batch.Batch; batch to add all the shapes to
    shape_batch = None

    def __init__(self, position, inventory=None, **kwargs):
        """Initialize a Mob at position.

        :type position: list
        :param position: location to place the mob
        :param inventory: (dict) optional inventory of the mob
        :param kwargs: optional keyword arguments
        """
        super(Mob, self).__init__(**kwargs)

        # the inventory is a defaultdict that maps item names to quantities

