import gc, weakref


# ==============================================================================
# -- Converter:  Helper class  -------------------------------------------------
# ==============================================================================

class Converter(object):

    def __init__(self, world):
        self.world = world
        self.actor_nodes = weakref.WeakValueDictionary()
        self.actor_model_nodes = weakref.WeakValueDictionary()
        self.map = world.get_map()
        self.transform = carla.Transform(carla.Location(x=0.0, z=0.0))
        self.navigation = world.get_navigation()
        self.walls = None
        self.crosswalks, self.sidewalks, self.roads, self.lanes = [], [], [], []
        self.avoids = []
        self.edges = set()
        self.get_road_hierarchy()
        # self.display_waypoints()

    def __call__(self, carla_actor):
        """
        Convert carla actor into encountered obstacle in the simulator
        """
        # If actor
