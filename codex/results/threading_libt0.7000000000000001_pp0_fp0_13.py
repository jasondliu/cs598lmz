import threading
threading.Thread(target=foo).start()
</code>
Note: 

<code>foo</code> is a method of <code>MainUI</code>, so <code>foo</code> has access to the class attributes, <code>foo</code> can access <code>self.window</code> so <code>self.window.start()</code> should work, but it does not.
<code>self.window.start()</code> raises an exception: <code>AttributeError: 'NoneType' object has no attribute 'start'</code>
<code>foo</code> is not a method of <code>QMainWindow</code>, so <code>self.window.start</code> should not be valid and so should raise the exception.
<code>self.window</code> is a pointer to <code>QMainWindow</code> object, so <code>self.window</code> should be able to call <code>start()</code>, but it does not.

Question
Why does <code>self.window</code> not call <code>start()</code>?

