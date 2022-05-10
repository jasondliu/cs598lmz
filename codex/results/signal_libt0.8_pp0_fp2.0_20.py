import signal
signal.signal(signal.SIGINT, handler)

def main(args):
    ##################
    # Input arguments
    ##################
    inputFile = args.inputFile
    outputFile = args.outputFile

    ############################
    # Open input and output files
    ############################
    with open(inputFile, 'r') as inputFileStream, \
            open(outputFile, 'w') as outputFileStream:

        #######################
        # Get data from inputs
        #######################
        t = int(inputFileStream.readline().strip())

        ##################
        # Output to screen
        ##################
        print("There are {} test cases.".format(t))

        ###########################
        # Iterate over test cases
        ###########################
        for testCase in range(t):
            n = int(inputFileStream.readline().strip())
            print("The test case #{} has n = {}".format(testCase, n))

            ################################
            # Calculate and write to outputs
           
