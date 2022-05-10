import ctypes
ctypes.cdll.LoadLibrary('../gurobi810/mac64/libgurobi_c++.a')
ctypes.cdll.LoadLibrary('../gurobi810/mac64/libgurobi81.so')

import gurobipy as gb
from gurobipy import GRB

#%%
#import build_data as bd
#
#data = bd.generate()
#
#num_intersects, num_actions, actions, min_g, max_g, min_y, max_y, min_r, max_r, u, G, Y, R, C, \
#intersect_mat, action_mat, term_mat, req_routes, req_dests, req_origs, starts, ends, turns = data
#
#num_requests, req_mat, req_inds = req_matrix_data(num_intersects, req_routes, req_dests, req_origs, u)

#%%
class TrafficGame():
    """
    Models a traffic decision game whose pay
