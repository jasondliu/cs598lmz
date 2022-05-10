import codecs
codecs.register_error("strict", codecs.ignore_errors) 
SAMPLE_RATE_MP3 = 44100
FEATURE_LENGTH_MP3 = 1024

def padding_audio(filename, song_len=100):
    p = pyaudio.PyAudio()
    stream = p.open(rate=SAMPLE_RATE_MP3,
                    format=p.get_format_from_width(2),
                    channels=2,
                    output=True)
    frames = []
    wf = wave.open(filename, 'rb')
    frames.append(wf.readframes(wf.getnframes()))
    frames = b''.join(frames)

    for i in range(0, int(song_len * SAMPLE_RATE_MP3 / 1024) - len(frames)):
        frames += b'\x00\x00'

    frames = np.frombuffer(frames, dtype="int16")
    stream.write(frames)

    stream.stop_stream()
    stream.close()
    p.terminate()

def mp3_to_m
