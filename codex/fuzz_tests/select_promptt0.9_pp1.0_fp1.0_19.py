import select
# Test select.select()
import socket
import Queue
socket.setdefaulttimeout(15)

# Following are dummy functions in the IPython sh shell namespace.
# Along with 'exit' they allow us to test multiple invocations of the shell.
ipsh.who_ls = lambda : []

def exit():
    pass
    # Exception that makes it look as if we hit EOF on stdin.
ipsh.ZMQExit = Exception

ipsh.history_level = 0
ipsh.input_splitter = IPython.core.inputsplitter.IPythonInputSplitter()
ipsh.input_transformer_manager = \
    IPython.core.inputtransformer.InputTransformerManager()

ipsh.init_ipython()
ipsh.hooks.late_startup_hook()
ipsh.autoindent = IPython.core.inputsplitter.IndentFilter(
    ipsh.input_splitter, ipsh
    )
ipsh.exit_now = False
ipsh.write = ipsh._write
ipsh.flush_input = lambda : None

# Make an application
