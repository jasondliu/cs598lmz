import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p)

def callback(userdata, level, msg):
    print("%d: %s" % (level, msg))

def main():
    # Initialize the library
    libvlc_instance = libvlc.Instance("--verbose=2")
    libvlc_log_set(libvlc_instance, FUNTYPE(callback), None)

    # Create a media player playing environement
    media = libvlc.Media.new_path(libvlc_instance, "http://www.youtube.com/watch?v=F5U6x5U6y9U")
    media_player = libvlc.MediaPlayer(media)

    # Play the media player
    media_player.play()

    # Sleep for 1000 milliseconds
    time.sleep(1000)

if __name__ == "__main__":
    main()
</code>

