import sys, threading

def run():
    file = open('/Users/ta/Documents/Research/temp/isoHunt.txt', 'r')
    lineCount = 0
    while True:
        line = file.readline()
        lineCount = lineCount + 1
        if lineCount % 1000 == 0:
            print lineCount
        if line == '':
            break
        print line
        command = "hadoop fs -test -d " + line
        (status, output) = commands.getstatusoutput(command)
        if status != 0:
            continue
        command = "hadoop fs -rmr " + line
        os.system(command)
        print command


if __name__ == '__main__':
  threading.stack_size(67108864) # 64MB stack
  sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
  thread = threading.Thread(target = run) # instantiate thread object
  thread.st
