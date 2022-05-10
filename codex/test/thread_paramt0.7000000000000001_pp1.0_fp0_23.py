import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\n'.join(data))).start()

# Run in a subprocess a process that is expected to exit quickly
# but possibly with errors (e.g. due to missing dependencies).
# Return the exit code.
def run_quick_process(cmd, **kw):
    from subprocess import Popen, PIPE
    proc = Popen(cmd, **kw)
    try:
        outs, errs = proc.communicate(timeout=1)
    except TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate()
    return proc.returncode

# Find the path to the top-level NEMO directory.
# Return None if NEMO is not found.
def find_nemo_dir():
    if sys.platform.startswith('win'):
        import glob
        import os.path
        default_dirs = glob.glob(r'C:\Users\Public\Documents\NEMOGCM')
