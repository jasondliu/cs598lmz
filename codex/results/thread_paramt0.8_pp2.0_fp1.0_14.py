import sys, threading
threading.Thread(target=lambda: sys.stdout.write('hoi\n')).start()
</code>
Now you have some breathing space to write the code.
EDIT:
From the comments it sounds like this is not what you're looking for. Here's some more info, but it may not help you:

There is no way to resume an operation that was suspended by <code>raw_input()</code>
There is no way to have a function accept arbitrary input: you have to pass it in as an argument.
This means you can't call a function and pass it <code>raw_input()</code> and expect it to finish at some point in the future.


