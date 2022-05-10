import sys, threading

def run():
    cv2.setMouseCallback("result", select_point)  # 设置鼠标回调函数
    while (1):
        cv2.imshow("result", img)
        key = cv2.waitKey(30) & 0xff
        if key == 27 or key == ord('q'):
            break
    cv2.destroyAllWindows()

def select_point(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # print("x: %s, y: %s" % (x, y))
        img_multiChannel[y, x] = [0, 255, 0]

if __name__ == '__main__':
    face_cascade = cv2.CascadeClassifier(r'./haarcascade/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(r'./haarcascade/haarcascade_eye.xml')

    img =
