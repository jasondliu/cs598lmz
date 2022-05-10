import sys, threading
threading.Thread(target=lambda: sys.stdout.write("This is printed\n")).start()
threading.Thread(target=lambda: sys.stdout.write("right before\n")).start()
threading.Thread(target=lambda: sys.stdout.write("This is printed\n")).start()
threading.Thread(target=lambda: sys.stdout.write("this is printed\n")).start()
threading.Thread(target=lambda: sys.stdout.write("right after\n")).start()

# This is printed
# right before
# this is printed
# This is printed
# right after
```

In normal operations, you shouldn't have to care about the order in which threads print to `sys.stdout`. But it can be an issue if you test your code (e.g., in an automated framework). In that case, you can obtain an ordering guarantee by setting a `threading.local()` object to a value before starting the thread and then waiting for that value to have been set by the thread after it stops running. The following code does this for the four threads in the example above:

``
