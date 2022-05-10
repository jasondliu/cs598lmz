import signal
# Test signal.setitimer() to see if it's there.
signal.setitimer

# In the following lines, try to import the platform-specific modules.
# If any module can not be imported, comment out the line that imports it and
# the line that initializes the appropriate variable to an empty list.
# This means that the platform-independent code will not be used on that
# platform, or will not use that feature, if any.
#
# If you downloaded the "pandokia-zephyr" package, it is already installed
# for you and the following line should work.  If you downloaded the "zephyr"
# package and installed it yourself, change the first part of the line to
# point to where you put it.
#
# If you downloaded a .zip file and unzipped it, you will need to put the
# directory "zephyr" somewhere it can be imported, and change the first part
# of the line to point to the new location.
#
# If you downloaded a tarball, you need to make a setup.py and install the
# package.  There is a setup.py in the tarball.
