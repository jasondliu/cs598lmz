import gc, weakref
import os, sys, time
import threading
import traceback

#
# !!! IMPORTANT !!!
#
# This module is imported by the main pygame module.
# This means any exceptions raised by this module will be
# caught by the pygame.init() function.
#

#
# Module Constants
#

# The default number of channels to use.
# This can be changed with the set_num_channels() function.
# It is also used to set the number of channels when the mixer
# is initialized.
_default_number_of_channels = 8

# The default size of the sound buffer.
# This can be changed with the set_buffer() function.
# It is also used to set the buffer size when the mixer
# is initialized.
_default_buffer_size = 4096

# The default frequency to use.
# This can be changed with the set_frequency() function.
# It is also used to set the frequency when the mixer
# is initialized.
_default_frequency = 22050

# The default sample size to use.
# This can be
