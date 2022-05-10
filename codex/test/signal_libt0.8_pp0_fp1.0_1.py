import signal
signal.signal(signal.SIGINT, lambda num,frame: sys.exit(0))

# Loop over all tiles in upper left quadrant
for iy in range(0, ntiles):
    for ix in range(0, ntiles):
        # Create file name and delete if it already exists
        fname = options.output_filename % (ix, iy)
        if os.path.exists(fname):
            os.remove(fname)

        # Loop over all times in the final image
        for i in range(0, len(good_times)):
            g = str(int(good_times[i]))
            
            # Get the subfile name
            sname = options.input_filename % (g, ix, iy)
            
            # Copy the file
            if os.path.exists(sname):
                shutil.copy(sname, fname)
