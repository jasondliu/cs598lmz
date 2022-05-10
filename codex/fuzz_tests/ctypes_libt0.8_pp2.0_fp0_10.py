import ctypes
ctypes.windll.user32.LockWorkStation()
</code>
I gather this is the closest thing to what you're after but you should be aware of the potential security implications and that this would be an extremely poor solution for any environment other than a single desktop.

