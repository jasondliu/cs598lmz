import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Foobar")).start()
</code>
Is this a viable strategy? It can create as many threads as needed without blocking the current thread. It won't necessarily block the current thread from writing to sys.stdout before the other thread starts, but the output will be interleaved regardless, and I doubt that there's any way to guarantee a specific order of output.
Another solution: use <code>logging.StreamHandler</code> to direct logging to any arbitrary stream, and create my own stream implementation that forwards output to sys.stdout and to a separate buffer. I can then <code>.flush()</code> the latter when I need to write that accumulated output to the destination file. Unfortunately, I also need to direct output of several 3rd-party libraries to the same stream, and changing my application logging configuration to use the custom stream means that I disrupt the other parts of the application that are still in development.


A:

I'm assuming that you want whatever function you're calling to print to stdout and also save the print output (in the order it was printed, but not necessarily in the order it was generated) to a file. 

