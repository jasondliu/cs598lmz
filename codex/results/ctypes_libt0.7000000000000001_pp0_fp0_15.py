import ctypes
ctypes.windll.user32.LockWorkStation()
</code>
Additionally you may need to add <code>PIPE_WAIT</code> to the <code>dwPipeMode</code> argument of <code>CreateNamedPipe</code>, so that the <code>ConnectNamedPipe</code> is blocking.

