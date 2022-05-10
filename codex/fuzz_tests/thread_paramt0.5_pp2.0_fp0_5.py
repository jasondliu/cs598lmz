import sys, threading
threading.Thread(target=lambda: sys.stdin.read(1)).start()

# import cv2
# import numpy as np
# import sys, threading
# threading.Thread(target=lambda: sys.stdin.read(1)).start()

# cap = cv2.VideoCapture(0)
# while True:
# 	_, frame = cap.read()
# 	frame = cv2.flip(frame, 1)
# 	cv2.imshow('frame', frame)
# 	k = cv2.waitKey(5) & 0xFF
# 	if k == 27:
# 		break

# cv2.destroyAllWindows()
# cap.release()

# import cv2
# import numpy as np
# import sys, threading
# threading.Thread(target=lambda: sys.stdin.read(1)).start()

# cap = cv2.VideoCapture(0)
# while True:
# 	_, frame = cap.read()
# 	frame = cv2.flip(frame
