import _struct

def read_wav(audio_file):
    wave_read = wave.open(audio_file)
    # print(wave_read.getparams())
    num_frames = wave_read.getnframes()
    num_channels = wave_read.getnchannels()
    framerate = wave_read.getframerate()
    num_samples_width = wave_read.getsampwidth()
    raw_data = wave_read.readframes(num_frames)
    wave_read.close()
    total_samples = num_frames * num_channels
    if num_samples_width == 1:
        fmt = "%iB" % total_samples  # read unsigned chars
    elif num_samples_width == 2:
        fmt = "%ih" % total_samples  # read signed 2 byte shorts
    else:
        raise ValueError("File has an unsupported bit-depth")
    integer_data = _struct.unpack(fmt, raw_data)
    del raw_data  # keep memory tidy (who knows how big it might be
