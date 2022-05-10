import ctypes
ctypes.windll.user32.SetProcessDPIAware()
#%%

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

#%%

def preprocessing(im):
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    _, im = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    im = cv2.medianBlur(im, 5)
    return im

def get_bbox(im):
    h, w = im.shape
    bbox = [w, h, 0, 0]
    for i in range(h):
        for j in range(w):
            if im[
