import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)
cv2.namedWindow('Demo Video')
cv2.namedWindow('Output Video')

vc = cv2.VideoCapture(r'C:\Users\moham\Desktop\opencv_image_processing\images\vtest.avi')

if vc.isOpened():
    is_capturing, _ = vc.read()
else:
    is_capturing = False

while is_capturing:
    try:
        is_capturing, frame = vc.read()
        cv2.imshow('Demo Video', frame)

        # The frame is ready and already captured
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        canny_frame = cv2.Canny(gray_frame, 100, 200)
        cv2.imshow('Output Video', canny_frame)
        cv2.waitKey(1)
    except:
        print('
