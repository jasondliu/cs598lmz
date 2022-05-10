import ctypes
ctypes.cdll.LoadLibrary('/usr/local/Cellar/opencv/4.4.0_1/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')

face_cascade = cv2.CascadeClassifier('/usr/local/Cellar/opencv/4.4.0_1/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')


# In[11]:


# 抽取图片中人脸并保存
def get_faces(path):
    # path为图片路径
    # 返回抽取的人脸列表
    faces = []
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.3,
