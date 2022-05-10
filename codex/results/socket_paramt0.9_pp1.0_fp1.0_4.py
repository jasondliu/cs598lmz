import socket
socket.if_indextoname('7') #'", "

###--- Injectable Socket Option Definitions ---###
# Set blind timeout in milliseconds (None or 0 means wait indefinitely)
blind_timeout = "None"

# Toggle verbosity of logging
verbose = True

# Set log level of verbosity
verbose_level = "DEBUG" # "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"

# Export program output
export = False

# Set export file path
export_file = "C:\passwords.txt"

# Set port range for scanning
port_range = "1-65535" #"1-10", "500", "20-500", "4000,5000"

# Set port scan timeout in milliseconds
timeout = 6000 #scan timeout in milliseconds

# Set hostname or IP address
host = "localhost" #"localhost", "8.8.8.8", "pi3rrot.me"

# Toggle proxy support
proxy = True

# Set proxy type (socks or http)
proxy_type = "http" #"http", "socks"

# Set IP
