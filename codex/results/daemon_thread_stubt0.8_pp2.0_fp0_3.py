import sys, threading

def run():
    sys.exit(sublime_plugin.run_command(sys.argv[1]))


threading.Thread(target=run).start()
</code>

