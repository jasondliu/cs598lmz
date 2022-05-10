import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\a')).start()

def get_scaled_fft_data(frames, f_s):
    # Scaling of FFT
    fft_data = np.fft.rfft(frames)
    fft_data = np.abs(fft_data) * 2 / np.prod(frames.shape)
    fft_data[0] = fft_data[0] / 2
    # Scaled frequency
    f_scale = np.arange(0, len(fft_data) / 2 + 1)
    f_scale = f_scale * f_s / np.prod(frames.shape)
    return fft_data, f_scale

def get_fft_amplitude(fft_data, f_scale, f_min, f_max, num_amplitudes):
    # Get fft amplitude
    fft_amplitude = []
    for i in range(num_amplitudes):
        f_min_ = f_min + (f_max - f_min)
