import gc, weakref, os, time

def return_path():
    """
    returns the path where sauron_core is located
    """
    print(os.path.dirname(__file__))
    return os.path.dirname(__file__)

def sauronWakeUp():
    """
    returns the eye of sauron
    """
    face = True
    if face == True:
        from sauron_modules import eye, mouth
        eye_thread = eye.EyeThread()
        mouth_thread = mouth.Mouth()
    else:
        from sauron_modules.face import build_face
        face1 = build_face(
            100,
            (400, 400),
            'Eye',
            ret_queue=True,
            kwargs={'dataset_folder':return_path()+'/config/data/'})
        face1.process.start()
        #face1_thread = Process(
        #    target=face1.build_all,
        #    name="face1_process",
        #    args=(face1.queue,
