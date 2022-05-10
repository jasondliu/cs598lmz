import socket

p = pyaudio.PyAudio()

vol_threshold = 100

def callback(in_data, frame_count, time_info, status):
    stream.write(in_data)
    return (in_data, pyaudio.paContinue)

def detect_silence(audio_segment, silence_threshold=vol_threshold, chunk_size=100):
    trim_ms = 0 # ms

    assert audio_segment.dBFS < 0

    while audio_segment.dBFS < silence_threshold and trim_ms < 1000:
        trim_ms += chunk_size
        audio_segment = audio_segment[chunk_size:]

    return trim_ms

def createAudioFile(stream, p, recordDuration, audioFileName):

    print('* recording')
    frames = []

    for i in range(0, int(44100 / 1024 * recordDuration)):
        data = stream.read(1024)
        frames.append(data)
    print('* done recording')

    stream.stop_stream()
    stream.close()
