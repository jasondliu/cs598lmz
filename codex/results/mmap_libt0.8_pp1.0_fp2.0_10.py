import mmap
from datetime import datetime

from pylab import *
from scipy import *
from scipy import optimize

from my_save import my_save
from my_plot import my_plot
from read_write_geometry import read_geometry, write_geometry
from write_arc import write_arc
from read_arc import read_arc

from scipy.interpolate import UnivariateSpline

from find_displacement_from_angle import find_displacement_from_angle

from read_write_geometry import read_geometry

from read_write_ncdf import read_ncdf, write_ncdf

from linear_algebra import rotation_matrix

from scipy.interpolate import UnivariateSpline


#my_save(save_name,"list")
#my_save(save_name,"list",1,2)
#my_save(save_name,"list",1,2,3)
#my_plot(save_name, 1, 2, "title", "xlabel", "ylabel", "leg
