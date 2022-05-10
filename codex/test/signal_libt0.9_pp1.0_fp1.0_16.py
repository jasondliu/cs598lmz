import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

#write an eeg file
def writeEEG(resultEEG, fileName):
    #writing to position
    try:
        with open(fileName,"wt") as f:
            for line in resultEEG:
                #record the data in new file
                f.write(str(line.duration) + " " + str(line.alpha) + " " + str(line.beta) + " " + str(line.theta) + " " + str(line.gamma) + "\n")
    except Exception as e:
        print(str(e))

#write an act file
def writeACT(resultACT, fileName):
    try:
        with open(fileName, "wt") as f:
            for line in resultACT:
                #record the data in new file
                f.write(line + "\n")
    except Exception as e:
        print(str(e))

#combine files
