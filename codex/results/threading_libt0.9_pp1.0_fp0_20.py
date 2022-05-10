import threading
threading.Thread(target=main).start()

# This method is useful if your main thread halts but you still want the process to terminate.
def idle():
    while True:
        time.sleep(1)

threading.Thread(target=idle).start()
</code>
I want the main function and idle function to run simultaneously and started from the main function. Also, I want the process to terminate only after the <code>main</code> function ends.
The problem with the above code is, the <code>main</code> function stops once the child processes in the <code>for</code> loop finish executing. I want to end it only when the for loop ends. How can I do it?
<code>def main():
    procs=[] #holds the process objects
    for i in range(2):
        pr=multiprocessing.Process(target=pr,args=(file,))
        procs.append(pr)
        pr.start()
    #I have already tried adding pr.join() 
    #to this method which only makes the main 
    #thread joins the
