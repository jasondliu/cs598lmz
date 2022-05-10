import threading
threading.stack_size(1024*1024*10)

class App(object):
    def __init__(self, video_source=0):
        self.video_source = video_source        
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read('trainer/trainer.yml')
        self.cascadePath = "haarcascade_frontalface_default.xml"
        self.faceCascade = cv2.CascadeClassifier(self.cascadePath);
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.id = 0
        self.names = ['None', 'Izhar', 'Dewa', 'Ivan', 'Paijo']
        self.cam = cv2.VideoCapture(self.video_source)
        self.cam.set(3, 640)
        self.cam.set(4, 480)
        self.min_W = 0.1*self.cam.get(3)
        self.min_H
