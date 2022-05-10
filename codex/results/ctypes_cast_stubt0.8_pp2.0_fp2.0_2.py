import ctypes
ctypes.cast(glfwGetCurrentContext(), ctypes.py_object).value # works!
ctypes.cast(glfwGetCurrentContext(), ctypes.py_object).value is glfwGetCurrentContext() # False
</code>
Question
Is there a more Pythonic way to get the current context in Python?


A:

What you've found is the direct translation of the C API, you're getting exactly the same pointer that GLFW uses internally.
There's no way to get a Python object for the window, because GLFW doesn't keep a reference to them. The window you pass to <code>glfwMakeContextCurrent</code> is an arbitrary Python object. When you create a window, you'd have to store a reference to it yourself, e.g. in a dictionary.
That's what Pyglet does:
<code># Create a new OpenGL context for the given window
def gl_create_context(self):
    ...
    if self.context:
        window = self._glfw_contexts[self.context]
        if window:
            glfwMakeContextCurrent(window)
</code>

