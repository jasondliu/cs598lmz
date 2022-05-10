import threading
threading.stack_size(32768)

def thread_proc(thread_num):
    global num_runs, local_counter, global_counter
    for i in range(num_runs):
        # Read global_counter, then increment it...
        a = global_counter
        b = a + 1
        # ...and write back new value.
        global_counter = b
        local_counter[thread_num] = local_counter[thread_num] + 1

# Main program starts here.
if __name__ == '__main__':
    # Number of parallel threads to spin up
    num_threads = 4
    # Number of times to update global_counter in each thread
    num_runs = 1000000
    # List to hold local_counter data from each thread
    local_counter = [0] * num_threads
    # Global counter variable
    global_counter = 0

    # Create and start the threads
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=thread_proc, args=(i,))
        threads
