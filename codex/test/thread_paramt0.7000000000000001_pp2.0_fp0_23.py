import sys, threading
threading.Thread(target=lambda: sys.stdin.read(1)).start()

# import readline
# import rlcompleter
# readline.parse_and_bind("tab: complete")

# import readline
# import code
# vars = globals().copy()
# vars.update(locals())
# shell = code.InteractiveConsole(vars)
# shell.interact()

# import sys
# import code
# code.interact(local=locals())

# import code
# code.interact(local=dict(globals(), **locals()))

# import pdb
# pdb.set_trace()

# from IPython import embed
# embed()

# import IPython
# IPython.embed()

# import pdb; pdb.set_trace()
