import threading
threading.local = threading.local()

from ci_helper import *

def status():
    """ Changes each repository's tracked branch to 'dev', checks out the
    repository, updates it, and pulls it. Then, it changes the tracked branch
    back and returns to the previous directory.
    """
    # Record the directory of each repository
    fp = os.popen("find . -maxdepth 2 -mindepth 2 -name .git -type d -printf '%h '")
    status_info = fp.read().split(" ")
    fp.close()
    status_info = sorted(status_info)

    # Determine if the log should show the command output for each
    # repository or not
    #log("\nDetermining if detailed output should be shown...")
    silent = (command("git config --get core.quiet && exit 0 || echo -n true") == "true")
    #log("Detailed output is turned " + ("off" * silent + "on" * (1-silent) + ".\n"))

    # Make a transaction by adding ".
