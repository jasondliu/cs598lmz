import sys, threading

def run():
    for arg in sys.argv[1:]:
        print arg
        # TODO: check if file exists
        output_file = open("output_" + arg, "wb")
        with open(arg, "rb") as input_file:
            interrupted = False
            while True:
                try:
                    print 'test'
                    line = input_file.readline()
                    print 'test2'
                except KeyboardInterrupt:
                    interrupted = True
                if line == "":
                    break
                print line
                output_file.write(line)
                output_file.flush()
        if interrupted:
            break
    output_file.close()

thread = threading.Thread(target=run)
thread.start()
thread.join()
