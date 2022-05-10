from bz2 import BZ2Decompressor
BZ2Decompressor()
</code>
This should not be happening.  Is this a bug in the bz2?  It is causing intermittent segfaults in the application.  On the other hand, it is possible that the application is doing something wrong with the bz2.  I don't know how to diagnose the issue.  Are there any known issues with the bz2?  Is there any known workaround?
Edit:  I am using
<code>Python 2.6 (r26:66714, Apr 26 2009, 11:39:14) 
[GCC 4.4.1] on linux2
</code>
Edit 2:  I should add that the application is multithreaded and has a lot of global variables, but no global bz2 objects.  The application crashes at completely random points.  I can't reproduce the crash with the same input.


A:

I'd start by checking that you aren't calling the constructor in a loop.  (Not that I see how that could cause a segfault, but it's worth checking.)

