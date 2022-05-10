import threading
threading.Thread(target=lambda : drive_in_box(drive, x_target=1, y_target=1, z_target=1, tolerance=0.5)).start()
threading.Thread(target=lambda : drive_in_box(drive, x_target=2, y_target=2, z_target=2, tolerance=0.5)).start()
 
 
 # Using the *thing* notation. 
 
