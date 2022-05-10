import codecs
codecs.register_error("strict", codecs.ignore_errors)


class Terminal:
    """
    Terminal class. A Terminal has a name, an address and a list of services.
    Optionally, it can have a list of realted bus stops.
    """

    def __init__(self, name, addr, services, stops=None):
        self.name = name
        self.addr = addr
        self.stops = stops
        self.services = services

    def __eq__(self, other):
        return self.name == other.name and \
               self.addr == other.addr and \
               self.stops == other.stops


class BusStop:
    """
    BusStop class. A BusStop has a list of terminals, a list of routes and a
    name.
    """

    def __init__(self, terminals, routes, name=None):
        self.terminals = terminals
        self.routes = routes
        self.name = name

    def __eq__(self, other):
        return self.terminals == other.terminals and \
               self
