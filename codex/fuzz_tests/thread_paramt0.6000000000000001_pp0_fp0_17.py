import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()
 
# ##############################################################
# ####################   PERFORMANCE   #########################
# ##############################################################
 
# ####################   TIME   #########################
 
# "time.process_time()" returns the process time (time spent by all threads)
# "time.perf_counter()" returns the real time (wall time)
 
import time
 
time.process_time()
time.perf_counter()
 
# "timeit" is another module to get performance
# documentation: https://docs.python.org/3/library/timeit.html
 
# ####################   MEMORY   #########################
 
# "memory_profiler" is a module to get the memory usage
# documentation: https://pypi.org/project/memory-profiler/
 
# ####################   LINE PROFILE   #########################
 
# "line_profiler" is a module to get time spent in each line of a function
# documentation: https://pypi.org
