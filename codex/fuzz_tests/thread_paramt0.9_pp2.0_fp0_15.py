import sys, threading
threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()

# ctrl-C to keep output to stdout but get prompt back
# ctrl-Z to pause the command, then fg to continue it
# ctrl-Z to pause it, then bg to run it in the background
# ctrl-Z to pause it, then disown to remove it from job list
# (leaving processes running even if shell is closed)

# > to redirect STDOUT to a file
# $ command > file.txt
# 0> or 1> to redirect just stdout or just stderr to a file

# >> to append STDOUT to end of a file

# file descriptor 2 is STDERR
# $ command 2> err.txt

# &> to redirect stdout and stderr to same file

# &>> to append stdout and stderr to same file

# $ command > file.txt 2> err.txt

# tee -a paginates output but appends it to an existing file

# ls | tee -a file.txt

# creating a job that runs in
