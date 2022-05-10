import signal
signal.signal(signal.SIGINT, keyboardInterruptHandler)

###############################################################################
##
##  Camera
##
###############################################################################

# Global vars
last_encoder_pos = None
ps2_last_state = ps2.PS2.INIT
visited_cells = []

# Initial images
im_left = camera.captureLeft()
im_right = camera.captureRight()

# Make the raw image black and white
im_left_bw = im_left.convert('L')
im_right_bw = im_right.convert('L')

# Convert the raw image to a numpy array
im_left_bw_np = np.array(im_left_bw)
im_right_bw_np = np.array(im_right_bw)

# Color information
color_left_int = color.ColorIntegrator(0)
color_right_int = color.ColorIntegrator(1)
color_sum_int = color.ColorIntegrator(2)
color_diff_
