import socket
import sys
import time
import csv
import threading
import os
import random
import math
import numpy as np
from collections import deque
from collections import Counter
from datetime import datetime
from datetime import timedelta

# Global variables

# The number of bytes in a message
message_size = 4096

# The number of bytes in a header
header_size = 4

# The number of bytes in a sequence number
seq_num_size = 4

# The number of bytes in a type
type_size = 4

# The number of bytes in a checksum
checksum_size = 4

# The number of bytes in a payload
payload_size = message_size - header_size

# The number of bytes in a sequence number
seq_num_size = 4

# The sequence number of the next message to be sent
next_seq_num = 0

# The sequence number of the next expected message
next_expected_seq_num = 0

# The number of messages sent
num_messages_sent = 0

# The number of messages received
num
