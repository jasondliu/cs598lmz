import sys, threading

def run():
    print("Hello")

def quickfire(targets, target_args, sandbox, native_objs):
    threads = []
    for x in range(0, targets): # for each thread
        #write args file
        args_file = 'args_' + str(x) + '.txt'
        f = open(args_file, 'w')
        for arg in target_args:
            f.write(arg + '\n')
        f.close()

        # run sandbox 
        threads.append(threading.Thread(target=sandbox, args=(args_file, native_objs,)))
        include_in_sandbox(args_file, safe_write=True)

    print("Launching threads...")
    for t in threads:
        t.start()

    print("Joining threads...")
    for t in threads:
        t.join()

    print("Tests complete!")
    return True

def sandbox(args_file, native_objs, code=None):
    args_file_path = './' + args_file

