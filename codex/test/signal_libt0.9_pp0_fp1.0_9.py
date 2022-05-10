import signal
signal.signal(signal.SIGINT, lambda signum, frame: sys.exit(0))

# For efficiency, we define an extra helper function that extracts
# the raw audio and returns it as a numpy array.
def get_wav_info(wav_file):
    rate, data = wavfile.read(wav_file)
    return rate, data

# For efficiency, we define an extra helper function that extracts
# the raw audio and returns it as a numpy array.
def read_wave(path):
    """Reads a .wav file.

    Takes the path, and returns (PCM audio data, sample rate).
    """
    with contextlib.closing(wave.open(path, 'rb')) as wf:
        num_channels = wf.getnchannels()
        assert num_channels == 2
        sample_width = wf.getsampwidth()
        assert sample_width == 2
        sample_rate = wf.getframerate()
        assert sample_rate in (16000, 44100)
        pcm_data = wf
