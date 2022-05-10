import threading
threading.Thread(target=run_server).start()

from keras.models import load_model
import cv2
import numpy as np

model = load_model("E:/FaceRecognition/facenet_keras.h5")

# load the known faces and embeddings
data = pickle.loads(open("E:/FaceRecognition/embeddings.pickle", "rb").read())

# load our serialized face detector from disk
print("[INFO] loading face detector...")
protoPath = "E:/FaceRecognition/face_detector/deploy.prototxt"
modelPath = "E:/FaceRecognition/face_detector/res10_300x300_ssd_iter_140000.caffemodel"
detector = cv2.dnn.readNetFromCaffe(protoPath, modelPath)

# load our serialized face embedding model from disk
print("[INFO] loading face recognizer...")
embedder = cv2.dnn.readNetFromTorch("E:/FaceRecognition
