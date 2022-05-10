import ctypes
import ctypes.util
import threading
import sqlite3


class dbscan(object):
    def __init__(self,
                 p_eps,
                 p_min_pts,
                 p_metric,
                 p_metric_arg,
                 p_dist_type,
                 p_dens_type,
                 p_theta,
                 p_delta,
                 p_nthreads):
        self.__lib = None
        self.__eps = p_eps
        self.__min_pts = p_min_pts
        self.__metric = p_metric
        self.__metric_arg = p_metric_arg
        self.__dist_type = p_dist_type
        self.__dens_type = p_dens_type
        self.__theta = p_theta
        self.__delta = p_delta
        self.__nthreads = p_nthreads
        self.__labels = None
        self.__n_clusters = 0

    def load_lib(self, p_lib_path):
        self
