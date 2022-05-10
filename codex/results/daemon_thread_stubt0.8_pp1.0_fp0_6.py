import sys, threading

def run():
    os.system('python ./bin/image_generator.py')

if __name__ == "__main__":
    # getting the number of processes
    nb_proc = int(sys.argv[1])

    # create a pool of processes
    pool = Pool(processes=nb_proc)

    # creating a list with the different computers that are going to run the process
    computers = []
    for i in range(nb_proc):
        computers.append(pool.apply_async(run, args=()))

    # starting the process
    for computer in computers:
        computer.get()

    # closing the pool
    pool.close()
    pool.join()
