import codecs
codecs.register_error("strict", codecs.ignore_errors)

from pyrocko import util, model
from pyrocko.guts_array import Array
from pyrocko.orthodrome import distance_accurate50m as distance
from pyrocko.gf import LocalEngine, Target


guts_prefix = 'pf.scenario'

km = 1000.
guts_to_pyrocko_map = {
    'strike': 'strike',
    'dip': 'dip',
    'rake': 'rake',
    'lat': 'lat',
    'lon': 'lon',
    'depth': 'depth',
    'm0': 'm_rr',
    'M0': 'm_rr',
    'p_arrival_time': 'p_time',
    's_arrival_time': 's_time',
    'DC': 'm_dc',
}

pyrocko_to_guts_map = {v: k for k, v in guts_to_pyrocko_map.items()}

pyrocko_lower_guts
