import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    z = ctypes.c_double

spacetime = lib.spacetime_new()

lib.spacetime_set_initial_time(spacetime, 0.0)
lib.spacetime_set_final_time(spacetime, 100.0)
lib.spacetime_set_time_step(spacetime, 0.1)

print lib.spacetime_get_initial_time(spacetime)
print lib.spacetime_get_final_time(spacetime)
print lib.spacetime_get_time_step(spacetime)

lib.spacetime_set_initial_position(spacetime, S(0.0, 0.0, 0.0))
lib.spacetime_set_initial_velocity(spacetime, S(1.0, 1.0, 1.0))

initial_position = lib.spacetime_get_initial_position(spacetime)
initial_velocity = lib.spac
