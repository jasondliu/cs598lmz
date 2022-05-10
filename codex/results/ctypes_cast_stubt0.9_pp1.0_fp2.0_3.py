import ctypes
ctypes.cast(cd_intervals_calc_values, ctypes.POINTER(ctypes.c_int))


for i in range(0, 1000):
  with transaction:
    bac_spike_calib_list[i] = t_spike[i].value()
    bac_spike_time_list[i] = time_array[i]


for i in range(0, 100):
  with transaction:
    bac_spike_calib_list[1000 + i] = t_spike_calib_vals[i].value()
    bac_spike_time_list[1000 + i] = calib_array[i]
