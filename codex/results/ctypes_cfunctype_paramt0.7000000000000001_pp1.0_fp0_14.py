import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_char_p,ctypes.c_int,ctypes.c_void_p,ctypes.c_void_p,ctypes.c_void_p)

def callback(buffer, frames, time, status):
    print(buffer.value)
    return 0

def capture(buffersize=1024):
    audio = ctypes.CDLL("libportaudio.so")
    audio.Pa_Initialize()

    inputParameters = PaStreamParameters()
    inputParameters.device = 0
    inputParameters.channelCount = 1
    inputParameters.sampleFormat = PA_SAMPLE_TYPE
    inputParameters.suggestedLatency = Pa_GetDeviceInfo(inputParameters.device).defaultLowInputLatency
    inputParameters.hostApiSpecificStreamInfo = None

    err = audio.Pa_OpenStream(ctypes.byref(stream), ctypes.byref(inputParameters), None, SAMPLE_RATE, FRAMES_PER_BUFFER, PA_FLAG,
                              callback, None)
    print(err)

    audio.
