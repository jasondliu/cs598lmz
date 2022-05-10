import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# ------------
# User Options
# ------------

# This option will print all the commands sent
# to the remote device to the console
DEBUG = 0

# This option enables the use of the
# aes-256-cbc cipher (required for the
# Cisco Nexus 5000 series)
ENABLE_AES = 1

# This option will save the configuration
# of the remote device to a file
SAVE_CONFIG = 1

# This option will run the script in
# simulation mode.  No commands will be
# sent to the remote device
SIMULATION = 0

# This option will save the output of
# the show commands in a file
SAVE_OUTPUT = 1

# This option will send an email when
# the script has finished running
SEND_EMAIL = 0

# This option will send an SNMP trap
# when the script has finished running
SEND_SNMP = 0

# This is the email address that will be
# used when sending emails
