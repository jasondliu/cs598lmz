import weakref
import math

#===============================================================================
#
# RotationPointGroup
#
#===============================================================================
class RotationPointGroup(object):
    def __init__(self, group_id, center_point, point_list):
        self.group_id     = group_id
        self.center_point = center_point
        self.point_list   = point_list
        self.grid_size    = 1.0
        self.marked       = False
    
    def get_group_id(self):
        return self.group_id
    
    def get_point_list(self):
        return self.point_list
    
    def get_center_point(self):
        return self.center_point
    
    def get_grid_size(self):
        return self.grid_size
    
    def is_marked(self):
        return self.marked
    
    def set_group_id(self, group_id):
        self.group_id = group_id
        
    def set_point_list(self, point_list):
