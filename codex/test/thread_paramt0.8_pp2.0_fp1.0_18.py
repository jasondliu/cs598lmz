import sys, threading
threading.Thread(target=lambda:sys.stdout.write("\x1b]2;[%s] %s\x07"%(__file__,__cwd__))).start()

import os
os.environ['PYTHONINSPECT'] = ' '


# import vispy.app, vispy.scene
#
# class Canvas(vispy.app.Canvas):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.unfreeze()
#         self._timer = vispy.app.Timer('auto', connect=self.on_timer, start=True)
#         self._timer.start()
#
#     def on_key_press(self, event):
#         print("Got key press:", event.text)
#
#     def on_mouse_press(self, event):
#         print("Got mouse press: ", event.button)
#
#     def on_timer(self, event):
#         print("Updating canvas", time.time())
#
