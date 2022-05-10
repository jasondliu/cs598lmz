import signal
signal.signal(signal.SIGINT, signal.default_int_handler)

# When you exit the shell the current app will remain open.
# At the moment there is not a way to exit the app when you exit the Python
# shell, so you can kill the app manually if this is desired.

# When you want to kill the app in the terminal use the command:
# $ killall Python

# For convenience, you might consider adding something like the following to
# your .bashrc:
# alias pyshell='/Applications/Python\ 3.7/Install\ Certificates.command;/Applications/Python\ 3.7/Update\ Shell\ Profile.command;python3.7'

# This will allow you to run 'pyshell' and be in the desired Python environment
# with access to all of the relevant packages without having to activate the
# virtual environment or install the shell profile and certificates.
import sys
import app
import ui
import helper
import io

################################################################################
# Useful functions


# The following two functions allow you to connect to a function as an
# action. See the
