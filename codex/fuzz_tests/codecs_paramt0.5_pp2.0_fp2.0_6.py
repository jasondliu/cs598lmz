import codecs
codecs.register_error("strict", codecs.ignore_errors)

class GtfsReader(object):
    def __init__(self,gtfs_path,service_ids_path,route_ids_path,stop_ids_path,timezone):
        self.gtfs_path = gtfs_path
        self.service_ids_path = service_ids_path
        self.route_ids_path = route_ids_path
        self.stop_ids_path = stop_ids_path
        self.timezone = timezone
        self.services = {}
        self.routes = {}
        self.stops = {}
        self.trips = {}
        self.stop_times = {}
        self.calendar = {}
        self.trips_per_service = {}
        self.stop_times_per_trip = {}
        self.routes_per_trip = {}
        self.stops_per_route = {}
        self.trips_per_route = {}
        self.trips_per_stop = {}
        self.stop_times_per
