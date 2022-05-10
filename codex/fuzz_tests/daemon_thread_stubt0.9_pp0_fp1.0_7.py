import sys, threading

def run():

    print '#####  starting Python threads not all blocked #####'
    # print '#####  running with threads not blocked ############'
    # print '#####  but threads in Python are paused  ############'
    # print '##       using time.sleep() between them           ##'
    # print '####################################################'
    print ''

    ## create some threads
    threads = []
    for thread_id in range(0,100) :
        thread = threading.Thread(target = one_threaded_cpu_intense_calc, args = (thread_id, ))
        threads.append(thread)

    # initialize all threads threads
    for thread in threads :
        thread.start()

    # wait for all threads to finish (this sleep does NOT pause Python threads)
    for thread in threads :
        thread.join()

    print '#####  DONE with Python threads #####'
    print '####################################################'


def one_threaded_cpu_intense_calc(thread_id):
    create_high_load_in_current_thread(5, thread
