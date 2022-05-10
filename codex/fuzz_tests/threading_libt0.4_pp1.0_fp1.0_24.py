import threading
threading.Thread(target=lambda: None).start()
</code>
It's not clear to me what the difference is between the two. Why is the second one needed?


A:

The first example creates a <code>threading.Thread</code> object, but doesn't start it. The second example actually starts the thread.

