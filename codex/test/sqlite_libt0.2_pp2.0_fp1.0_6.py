import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os

#
# This is a simple example of how to use the libspotify API to
# log in and play a track.
#
# You will need a Spotify Premium account, and you'll need to register
# your application at https://developer.spotify.com/my-applications
#
# This example is built against libspotify 12.1.51 which is the latest
# version at the time of writing.
#
# Documentation about the libspotify API can be found at:
# https://developer.spotify.com/technologies/libspotify/docs/12.1.51/
#
# The libspotify source code can be found at:
# https://developer.spotify.com/download/libspotify/
#
# Compile this example with:
# gcc -o sp-example sp-example.c -lspotify -lpthread
#
# On Linux, you will also need to link against libasound.
#
# On Mac OS X, you will need to link against CoreFoundation and AudioToolbox.
#
# On
