import sys, threading

def run():
    for i in range(100):
        if i % 10 == 0:
            sys.stdout.write("\r{}".format(round((i / 100) * 100, 0)))
            sys.stdout.flush()

thread = threading.Thread(target=run)
thread.start()
</code>
A line of asterisks (******) appear and print, but the percentage doesn't. Shouldn't they be alternating, since they're in two different calls to sys.stdout, and there's a flush() between them?
Am I correct that it's possible to create something like a progress bar, where percentage updates are interlaced with the progress indicator?


A:

The <code>flush</code> method is horrible for this sort of thing. It does work but only when specifically called, and that contradicts the whole purpose of a progress bar.
If you want the percentage to be updated as it advances, you need to find a way for the output of the for loop to be <code>\r</code> on the same line. so something like this should work:
<code>def run():
    for i in
