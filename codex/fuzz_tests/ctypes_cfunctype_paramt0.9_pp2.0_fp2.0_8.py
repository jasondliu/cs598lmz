import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Get the MPI rank and size
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Initialize the Python layers
if rank == 0:
  print("Initializing the Python layers")
  bm.create_bmi()
  bm.initialize_config_file("flow_over_topo.yaml")
  bm.update_frac(0.0)

# Initialize the underlying model
bm.initialize()

# Initialize the coupling variable arrays
n_values = bm.get_var_count("land_surface__elevation")
land_elevation = numpy.zeros([n_values], numpy.float)
bm.get_var("land_surface__elevation", land_elevation)
water_level = numpy.zeros([n_values], numpy.float)
bm.get_var("sea_surface_height", water_level)
land_elevation = comm
