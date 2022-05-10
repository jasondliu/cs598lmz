import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

def image_show(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def convert_to_gray(color_img):
    gray = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
    return gray

def convert_to_hsv_color_space(color_img):
    hsv = cv2.cvtColor(color_img, cv2.COLOR_BGR2HSV)
    return hsv

def convert_to_lab_color_space(color_img):
    lab = cv2.cvtColor(color_img, cv2.COLOR_BGR2LAB)
    return lab

def convert_to_yuv_color_space(color_img):
    yuv = cv2.cvtColor(color_img, cv2.COLOR_
