import threading
threading.stack_size(20000)


def adjust_for_ambient_noise(source, duration=1):
    """
    re
    :param source:
    :param duration:
    :return:
    """
    print(u"adjusting for ambient noise")
    r.adjust_for_ambient_noise(source, dura

def callback(recognizer, audio):
    """
    callback 정의. 인자로는
    :param recognizer:
    :param audio:
    :return:
    """
    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
        if "오렌지 자니
