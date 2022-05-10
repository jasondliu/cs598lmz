import signal
signal.signal(signal.SIGINT, sigint_handler)

#Connect to Nao
##tts = ALProxy("ALTextToSpeech","nao.local", 9559)
##tts.setLanguage("English")
##tts.say("Hello")
##motion = ALProxy("ALMotion","nao.local", 9559)
##motion.wakeUp()
##motion.moveInit()
##memory = ALProxy("ALMemory","nao.local", 9559)
##motion.rest()
##motion.setStiffnesses("Body",0.0)

#Load the image
testImg = cv2.imread('t/sailor.png')

#Create the detector and tracker
detector = dlib.simple_object_detector("detector.svm")
tracker = dlib.correlation_tracker()

#Tracker initialization
win = dlib.image_window()
win.clear_overlay()
win.set_image(testImg)

#Run the detector and get the highest scoring detection.
