import sys, threading
threading.Thread(target=lambda: sys.stdout.write(sys.stdin.readline())).start()

# The above code is just a way of doing 
# python3 solution.py < input.txt > output.txt

#import sys
#for line in sys.stdin:
#    # process line
#sys.stdin.readline()

# another way of doing the above code is
# python3 solution.py < input.txt | tee output.txt

# this is a way to read from the standard input 
# and write to the standard output

# for reading from the file
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

# this is a way to read from the file
# and write to the file

# for reading from the file
# inputFile = open('input.txt', 'r')
# sys.stdin = inputFile

# for writing to the file
# outputFile = open('output.txt', 'w')
# sys.stdout = outputFile

# this is a way to
