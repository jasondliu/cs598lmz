import signal
# Test signal.setitimer call
signal.setitimer(signal.ITIMER_PROF, 0.001, 0.001)
# or
signal.setitimer(signal.ITIMER_REAL, 0.001, 0.001)
</code>
Ensure there is enough heap-space available for your JVM 
<code>java -Xmx=2G
</code>
Disable any watchdog software on the box - this is just a guess on my part, but these watchdog services may be messing with your signals.
If you are trying to implement a watchdog yourself, then it may be worth involving some native code, e.g. 

Jna (great, but a big project)
Jolie (not sure if this has what you need, but it is lightweight, check their language reference)
Your own JNI interface: Java Native Interface Specification 


