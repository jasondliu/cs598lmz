import signal
signal.signal(signal.SIGINT, signal_handler)

save_folder = 'output'
if not os.path.exists(save_folder):
    os.makedirs(save_folder)
    
filename = 'test'

# Loads file
file_name = 'test.avi'
print ('[+] File opened')
print ('[+] File name: %s'%file_name)

# Opens file
vidcap = cv2.VideoCapture(file_name)
vidcap.set(1,5)
success, image = vidcap.read()
success,image = True, cv2.imread("frame5.jpg")

# PrevImage
print ('[+] Image loaded')
print ('[+] Size: %sx%s'%(str(image.shape[0]),str(image.shape[1])))

# PrevSize
org_x = image.shape[0]
org_y = image.shape[1]

# PrevHW
