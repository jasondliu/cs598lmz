import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Windows Terminal")
#开始WebCam抓取
imgs = []
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame,1)
        imgs.append(frame)
    else:
        break
cap.release()

#让透亮度变高，截取上部分
for i in range(len(imgs)):
    imgs[i] = imgs[i][30:300,60:300]
    imgs[i][imgs[i]<128] = 0
    imgs[i][imgs[i]>=128] = 1
    imgs[i] = np.array(imgs[i]*255,dtype=np.uint8)
    imgs[i] = imgs[i].astype('uint8')

#获取摄
