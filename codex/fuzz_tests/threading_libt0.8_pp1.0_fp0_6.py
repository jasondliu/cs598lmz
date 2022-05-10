import threading
threading.thread(target=the_thread_func, name =  "My name is" + str(i), args = (i,))
</code>
I mean you pass an argument to a function that you pass to the threading.Thread constructor.

