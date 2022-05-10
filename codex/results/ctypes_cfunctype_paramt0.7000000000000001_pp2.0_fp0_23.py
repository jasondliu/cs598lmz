import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int)
cfunc = FUNTYPE(print_int)

# Set to TRUE on shutdown
shutdown = False

# Default sample rate
sample_rate = 44100

# Default buffer size
buffer_size = 512

# Default audio driver
audio_driver = 'portaudio'

# Initialize the sample rate, buffer size and audio driver
def init(sr=44100, bs=512, ad='portaudio'):
	global sample_rate, buffer_size, audio_driver
	sample_rate = sr
	buffer_size = bs
	audio_driver = ad
	# Initialize portaudio
	if ad == 'portaudio':
		pa_initialize()

# Shutdown audio
def shutdown_audio():
	global shutdown
	shutdown = True

# Callback for portaudio
def pa_callback(input_buffer, output_buffer, frame_count, time_info, status_flags, user_data):
	global shutdown, sample_rate
	# Shutdown if requested
	if shutdown:
		return paComplete

	for i
