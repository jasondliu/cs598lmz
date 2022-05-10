import sys, threading

def run():
    cmd = 'python -u %s/%s' % (os.getcwd(), sys.argv[1])
    os.popen(cmd, 'r')

thread = threading.Thread(target=run)
thread.start()
</code>
Then I renamed it and put it in my /bin and made it executable, then called 'thread run.py' from the command line. 
I was not getting the output from the subprocess, but if I called 'python run.py' the output of the program would show up in the console. 
What is keeping the output from showing up using thread.py? I would think it's because the subprocess is outputting data to stdout, but I'm not sure how to fix that. 

