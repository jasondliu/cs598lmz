import sys, threading
threading.Thread(target=lambda: m.moveto(0, 0), args=[]).start() # do not wait for this task
```

##### Calibrating

Once the RoboPair system is physically installed **the image should be well visible in the camera feed**. If not, the purpose of the `calibrate` subcommand is to let the user set visual parameters accordingly. Indeed, this command starts the camera feed, allows to set different parameters (such as gain, egain, shutter and exp) and produces an image after each change. Once the image looks good, the user can simply stop the process and parameters are saved in the setup file.

```
$ ./pair_robot_control.py calibrate
```

## Help

```
$ ./pair_robot_control.py -h
```
