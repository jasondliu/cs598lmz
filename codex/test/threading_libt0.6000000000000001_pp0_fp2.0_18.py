import threading
threading.stack_size(67108864)

# Set the number of threads
num_threads = 4

# Set the threading lock
threads_lock = threading.Lock()

# Set the number of stations
num_stations = 9

# Set the number of stations with data
num_stations_with_data = 0

# Set the number of stations with data
num_stations_with_data_lock = threading.Lock()

# Set the number of stations with data
num_stations_with_data_condition = threading.Condition()

# Set the number of stations with data
num_stations_with_data_barrier = threading.Barrier(num_threads)

# Set the number of stations with data
num_stations_with_data_barrier_lock = threading.Lock()

# Set the number of stations with data
num_stations_with_data_barrier_condition = threading.Condition()

# Set the number of stations with data
num_stations_with_data_barrier_flag = False

